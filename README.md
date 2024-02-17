# caleasy v1.0.0
Python CLI Client for Google Calendar

## Setup 
1. Enable Google Calendar
2. Create + download application `credentials.json`
`credentials.json` should look this: 
```json
{
    "installed": {
        "client_id": "JUST_AN_EXMPLE.apps.googleusercontent.com",
        "project_id": "caleasy",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": "THE_CLIENT_SECRET",
        "redirect_uris": [
            "http://localhost"
        ]
    }
}
```
3. Configure Oauth consent screen
4. Create test user (e.g. `name@youremail.com`)
5. Add scopes (`/auth/calendar`)

