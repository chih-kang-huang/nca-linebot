# NCA-Linebot

NCA Line Bot. A fork from github.com/jackyh1999/line_bot 

## Useful commands for deployment
- ```flyctl launch``` to launch a new app.
- ```flyctl deploy``` to deploy the app.
- ```flyctl logs```  useful for debugging

# Secrets

```
flyctl secrets set LINE_CHANNEL_SECRET=xxxxx LINE_CHANNEL_ACCESS_TOKEN=yyyyy
```
You can set several secret environment variables at once and it will automatically deploy after the execution.

 <!--- ## Data 
<!---Read only data are store temporarily in a [Google Sheet](https://docs.google.com/spreadsheets/d/1OZaZYPPFPVo5EuThuyjS3STR8nMf7peSjK673_bPDHE/edit#gid=0) --->
