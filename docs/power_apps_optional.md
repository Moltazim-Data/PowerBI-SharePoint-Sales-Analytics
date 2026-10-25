# Optional Power Apps basics exercise

This is an optional exercise; it is not implemented by the repository itself.

## Goal
Build a simple canvas form that creates a record in a SharePoint list and confirm the record was saved.

## Suggested SharePoint list: PipelineRequests
- Title — single line of text (required)
- Segment — choice (SMB, Mid-Market, Enterprise)
- LeadSource — choice (Inbound, Outbound, Partner, Paid Search, Referral)
- EstimatedAmount — currency
- RequestDate — date
- Status — choice (New, In Review, Approved, Rejected)

## Steps
1. Create the list in a site where you have permission.
2. In Power Apps, create a canvas app from the list or use the list's Integrate > Power Apps option if available.
3. Add fields and configure required inputs.
4. Submit a test request and verify it appears in the SharePoint list.
5. Test missing required values and confirm the app gives useful feedback.
6. Capture screenshots only after removing private site names, email addresses, and tenant details.

Add “Power Apps (Basics)” to your CV only after completing and testing the form yourself.
