# Power BI dashboard build guide

## 1. Prepare the workbook
1. Open `data/sales_opportunities.csv` in Excel.
2. Save a copy as `Sales_Opportunities.xlsx`.
3. Select the data and choose **Format as Table**. Confirm headers are enabled and name the table `OpportunitiesTable` under Table Design.
4. Upload the workbook to a document library in your SharePoint site or to OneDrive for Business.
5. Open it in Excel for the web once to verify access.

Use a work/school Microsoft 365 account if your organization's connector and sharing policies require it. Do not put private tenant URLs or credentials in this repository.

## 2. Connect Power BI Desktop
- **SharePoint Folder path:** choose Get Data > SharePoint Folder and enter the SharePoint **site URL**, not a link copied from the file-sharing dialog. Sign in with Organizational account, filter the file list by workbook name/folder, then combine or select the workbook content.
- **OneDrive for Business:** use the supported organizational cloud-file connection workflow available in your Power BI Desktop environment. Connector choices can vary by version and tenant policy.
- **Local fallback:** use Get Data > Excel or Text/CSV to practise the data model before cloud authentication is available.

Select the `OpportunitiesTable` table and rename the query/table to `Opportunities`.

## 3. Power Query checks
- Set `CreatedDate` and `CloseDate` to Date.
- Set `AmountEUR` to Decimal Number (or Fixed Decimal Number).
- Set all category and identifier fields to Text.
- Check that `OpportunityID` has no nulls and no duplicates.
- Leave blank CloseDate values for open opportunities.
- Choose Close & Apply.

## 4. Add DAX measures
Open Modeling > New measure and create each measure in `measures.dax` separately. Format the EUR measures as Euro currency and `Win Rate` as Percentage.

For the optional close-date trend, create a Calendar table, mark it as a date table, create an active relationship from Calendar[Date] to Opportunities[CreatedDate], and an inactive relationship from Calendar[Date] to Opportunities[CloseDate]. Then use the provided USERELATIONSHIP measure. Ensure the relationship columns are date-compatible.

## 5. Build one report page
Recommended layout:
1. **Top KPI row:** Total Opportunities, Open Pipeline EUR, Closed Won Amount EUR, Win Rate.
2. **Stage chart:** clustered bar chart; Stage on axis and distinct count of OpportunityID as values.
3. **Source chart:** LeadSource on axis and Win Rate as values.
4. **Trend chart:** Calendar month on axis and Closed Won Amount by Close Date EUR as values (after setting up the Calendar table and relationships).
5. **Slicers:** Segment, Region, SalesRep.
6. Use clear chart titles, EUR formatting, readable labels, and consistent spacing.

## 6. Test before sharing
- Confirm Total Opportunities equals the distinct ID count in the source.
- Open Pipeline excludes Closed Won and Closed Lost.
- Win Rate uses closed wins plus closed losses as its denominator; open deals are excluded.
- Slicers filter all expected visuals.
- Edit a harmless test value in the cloud workbook and test refresh if supported.
- Capture a clean report screenshot with no private account, tenant, or site details.
- Save the actual report in Power BI Desktop as `Sales_Pipeline_Overview.pbix`.

## Portfolio evidence
Keep the screenshot in `docs/screenshots/` after removing private details. Add a short note about what you learned, which connector path you used, and whether refresh was tested. Do not claim a published workspace, scheduled refresh, or gateway unless you configured and tested it.
