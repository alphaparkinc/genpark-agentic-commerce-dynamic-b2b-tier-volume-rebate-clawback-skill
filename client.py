# -*- coding: utf-8 -*-
"""B2B Tier Volume Rebate & Clawback Settler for GenPark Agentic Commerce."""
import json
from typing import Dict, Any

class B2BTierVolumeRebateClawbackSettler:
    @staticmethod
    def calculate_annual_bracket_volume_rebate(annual_spend_usd: float, tier_thresholds: Dict[str, float]) -> Dict[str, Any]:
        # Sort tiers ascending
        tiers = sorted(tier_thresholds.items(), key=lambda x: float(x[0]))
        earned_pct = 0.0
        active_tier_name = "Base Tier (0%)"
        
        for thresh_str, rate in tiers:
            thresh = float(thresh_str)
            if annual_spend_usd >= thresh:
                earned_pct = rate
                active_tier_name = f"Tier >= ${thresh:,.0f} ({rate}%)"
                
        rebate_payout_usd = round(annual_spend_usd * (earned_pct / 100.0), 2)
        return {
            "annual_spend_usd": annual_spend_usd,
            "qualified_tier": active_tier_name,
            "rebate_rate_pct": earned_pct,
            "earned_rebate_payout_usd": rebate_payout_usd,
            "settlement_instrument": "DISBURSEMENT_CREDIT_MEMO"
        }

    @staticmethod
    def reconcile_shortfall_rebate_clawback(contracted_tier_rebate_pct: float, actual_earned_tier_rebate_pct: float, actual_annual_spend_usd: float) -> Dict[str, Any]:
        shortfall_pct = max(0.0, contracted_tier_rebate_pct - actual_earned_tier_rebate_pct)
        clawback_amount_usd = round(actual_annual_spend_usd * (shortfall_pct / 100.0), 2)
        
        return {
            "contracted_rebate_pct": contracted_tier_rebate_pct,
            "actual_earned_pct": actual_earned_tier_rebate_pct,
            "shortfall_spread_pct": shortfall_pct,
            "net_clawback_payable_usd": clawback_amount_usd,
            "settlement_action": "ISSUE_DEBIT_MEMO_CLAWBACK" if clawback_amount_usd > 0 else "NO_CLAWBACK_TARGET_MET"
        }
