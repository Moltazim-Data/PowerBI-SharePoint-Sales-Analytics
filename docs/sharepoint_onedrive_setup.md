# SharePoint / OneDrive setup notes

1. Convert `sales_opportunities.csv` to an Excel workbook named `Sales_Opportunities.xlsx`.
2. Create an Excel table named `OpportunitiesTable`.
3. Upload it to your own OneDrive for Business or a SharePoint document library.
4. Use the connector supported by your Power BI Desktop and tenant setup. For SharePoint Folder, provide the site root URL rather than a file-sharing URL.
5. Authenticate with your permitted organizational account. Never store passwords, tokens, or private URLs in Git.
6. Validate the report refresh in your environment; successful connection once does not prove scheduled refresh is configured.

If you only have a personal Microsoft account, some organizational connectors or publishing features may not be available. You can still practise locally with the CSV/Excel file and complete the cloud step later.
