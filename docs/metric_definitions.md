# Metric definitions

| Metric | Definition | Interpretation / caveat |
|---|---|---|
| Total Opportunities | Distinct count of OpportunityID | Count of records in the opportunity table |
| Open Pipeline EUR | Sum of AmountEUR excluding Closed Won and Closed Lost | Unweighted value, not a probability-weighted forecast |
| Closed Won Amount EUR | Sum of AmountEUR where Stage = Closed Won | Opportunity amount proxy; not recognized accounting revenue |
| Closed Won Count | Distinct opportunities at Closed Won | Closed-won volume |
| Closed Lost Count | Distinct opportunities at Closed Lost | Closed-lost volume |
| Win Rate | Closed Won Count / (Closed Won Count + Closed Lost Count) | Excludes open opportunities; blank if there are no closed deals |
| Average Won Deal EUR | Average AmountEUR for Closed Won | Sensitive to deal mix and outliers |
| Median Won Sales Cycle Days | Median days from CreatedDate to CloseDate for Closed Won | Won deals only; excludes open opportunities |

## Interpretation guidance
- Always compare like-for-like segments and time periods.
- Do not label opportunity amount as booked or recognized revenue without defining the organization's accounting rules.
- Open pipeline value is not a forecast unless probability and timing assumptions are explicitly modeled.
- Win rate can change due to lead mix, deal size, and sales process changes; it is not a standalone performance diagnosis.
