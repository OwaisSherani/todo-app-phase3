# Connecting to Neon Database

This guide explains how to connect your Todo app to a Neon PostgreSQL database.

## Setting up Neon Database

1. **Create a Neon Account**:
   - Go to [https://neon.tech](https://neon.tech)
   - Sign up for a free account

2. **Create a Project**:
   - Log in to your Neon dashboard
   - Click "New Project"
   - Choose a region closest to your users
   - Select PostgreSQL version (14+ recommended)

3. **Get Connection Details**:
   - Once your project is created, go to the "Connection Details" section
   - Note down the connection string in the format:
     ```
     postgresql://username:password@ep-xxxxxx.region.provider.neon.tech/dbname?sslmode=require
     ```

## Updating Environment Variables

1. **Locate the .env file**:
   - In your project root: `backend/.env`

2. **Update the DATABASE_URL**:
   ```env
   # Replace with your actual Neon database connection string
   DATABASE_URL=postgresql://username:password@ep-xxxxxx.region.provider.neon.tech/dbname?sslmode=require
   
   # Other required environment variables
   COHERE_API_KEY=your_cohere_api_key
   SECRET_AUTH_KEY=your_secret_auth_key
   BETTER_AUTH_SECRET=your_better_auth_secret
   ```

## Testing the Connection

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   python main.py
   ```

3. **Verify the connection**:
   - Check the logs for successful database connection messages
   - The application should create the required tables automatically on startup

## Troubleshooting

### Common Issues:

1. **SSL Connection Errors**:
   - Ensure `?sslmode=require` is appended to your connection string
   - Neon requires SSL connections

2. **Authentication Failures**:
   - Verify your username and password are correct
   - Check for typos in the connection string

3. **Connection Timeout**:
   - Verify your internet connection
   - Check if your IP address is not blocked

### Enable Database Logging:

To enable SQL query logging for debugging, set the following in your .env:
```env
DB_ECHO=true
```

## Security Best Practices

1. **Never commit .env files** to version control
2. **Use strong passwords** for database access
3. **Rotate credentials regularly**
4. **Monitor database access logs** in your Neon dashboard
5. **Use connection pooling** (already configured in this application)

## Migrating Existing Data

If you're migrating from another database:

1. Export your current data
2. Update the DATABASE_URL to point to Neon
3. Restart the application to create tables
4. Import your data using Neon's migration tools or pg_restore

## Support

For Neon-specific issues, visit:
- [Neon Documentation](https://neon.tech/docs)
- [Neon Support](https://neon.tech/support)