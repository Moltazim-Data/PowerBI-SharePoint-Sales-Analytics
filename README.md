# Power BI + SharePoint Sales Analytics

A practical portfolio project for Data Analyst and BI Analyst roles. The project demonstrates how to prepare sales pipeline data, define reliable business KPIs with DAX, and build a Power BI report from an Excel workbook hosted in SharePoint or OneDrive for Business.

> **Data disclaimer:** all records are synthetic and fictional. Opportunity amounts are not recognized accounting revenue. This repository contains starter assets and build instructions; it does not contain a native `.pbix` report or a live Microsoft 365 connection.

## Project objectives
- Build an interactive sales pipeline overview with clear KPI definitions.
- Practice Power Query data typing and data quality checks.
- Use DAX for open pipeline, closed-won amount, win rate, average won deal size, and median sales cycle.
- Document a cloud-hosted Excel workflow using SharePoint or OneDrive for Business.
- Provide a reproducible, interview-friendly project with transparent limitations.

## Repository map
- `data/sales_opportunities.csv` — synthetic practice dataset (300 opportunities).
- `powerbi/measures.dax` — starter DAX measures.
- `powerbi/dashboard_preview.html` — interactive browser preview using the embedded synthetic dataset (not a `.pbix`).
- `powerbi/dashboard_build_guide.md` — step-by-step report construction.
- `docs/data_dictionary.md` — field definitions.
- `docs/metric_definitions.md` — KPI formulas and caveats.
- `docs/sharepoint_onedrive_setup.md` — cloud-source setup notes.
- `docs/power_apps_optional.md` — optional SharePoint list + Power Apps exercise.
- `docs/cv_wording.md` — accurate CV wording to use only after completing the work.

## Quick start
1. Download `data/sales_opportunities.csv` and open it in Excel.
2. Convert the data range to an Excel Table named `OpportunitiesTable`.
3. Save as `Sales_Opportunities.xlsx` and upload it to your own OneDrive for Business or SharePoint document library.
4. Open Power BI Desktop and connect to the hosted workbook using the connector path supported by your Microsoft 365 environment. If cloud authentication is unavailable, start locally with the CSV.
5. Load the table as `Opportunities`, confirm data types, and follow the build guide.
6. Add measures from `powerbi/measures.dax`, create the visuals, and test all slicers.
7. Save your work as `Sales_Pipeline_Overview.pbix` on your own machine.

## Suggested report layout
- KPI cards: Total Opportunities, Open Pipeline EUR, Closed Won Amount EUR, Win Rate.
- Bar chart: opportunity count by stage.
- Bar chart: win rate by lead source.
- Trend: closed-won amount over time (use CloseDate relationship for a true close-date trend).
- Slicers: Segment, Region, SalesRep.

## Validation checklist
- OpportunityID is unique and nonblank.
- CreatedDate and CloseDate are date types; AmountEUR is decimal/currency.
- Open Pipeline excludes Closed Won and Closed Lost.
- Win Rate denominator includes only closed-won plus closed-lost deals.
- Visuals respond to Segment, Region, and SalesRep slicers.
- Any cloud refresh is tested rather than assumed.

## Limitations
This repository does not claim a completed native Power BI file, configured scheduled refresh, gateway, deployed Power App, or access to any private tenant. Complete and test those steps in your own environment before listing them as hands-on experience.

## Analysis report
See [reports/portfolio_report.md](reports/portfolio_report.md) for the report structure, business questions, interpretation caveats, and recommended next actions.
