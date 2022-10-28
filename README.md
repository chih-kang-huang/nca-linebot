# NCU-Line-bot

## Useful commands for deployment
- ```flyctl launch``` launches the new app.
- ```flyctl deploy``` to deploy the app.
- ```flyctl logs``` is useful for debugging

# Screts

```
flyctl secrets set LINE_CHANNEL_SECRET=xxxxx LINE_CHANNEL_ACCESS_TOKEN=yyyyy SHEET_ID=zzzzzz
```
You can set several secret environment variables at once and it will automatically deploy after the execution.

## Data
Read only data are store temporarily in a [Google Sheet](https://docs.google.com/spreadsheets/d/1OZaZYPPFPVo5EuThuyjS3STR8nMf7peSjK673_bPDHE/edit#gid=0)
