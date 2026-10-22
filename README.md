# B2B Dynamic Tier Volume Rebate & Clawback Settlement Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

B2B annual procurement bracket tier rebate, retro-active rebate clawback if annual minimum threshold missed, and credit memo reconciler. Built for GenPark (https://www.genpark.ai).

## 🌐 Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## 🛠️ MCP Tools Exposed
- `calculate_annual_bracket_volume_rebate`: Calculate progressive or cliff volume rebate based on customer accumulated annual spend.
- `reconcile_shortfall_rebate_clawback`: Calculate clawback penalty and invoice adjustment if customer upfront discounts exceeded actual realized tier.

## 🚀 Installation & Usage
```bash
python -m genpark_agentic_commerce_dynamic_b2b_tier_volume_rebate_clawback_skill.server --test
```
