# Render Deployment Guide

## Prerequisites
- GitHub account with the project repository
- Render account (https://render.com)
- Your GEMINI_API_KEY ready

## Step-by-Step Deployment

### 1. Push to GitHub
```bash
git add .
git commit -m "Add Render deployment configuration"
git push origin main
```

### 2. Create Render Service
1. Go to https://dashboard.render.com
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Select the repository containing this project

### 3. Configure the Service
- **Name**: `shl-assessment-agent` (or your preferred name)
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- **Plan**: Free (or Pro for better performance)

### 4. Set Environment Variables
In the **Environment** section, add:
```
GEMINI_API_KEY=AIzaSyAce8PzoPWVVxRN1LzePIyYTyqWD6W5h5c
```

### 5. Deploy
- Click **"Create Web Service"**
- Render will automatically build and deploy your service
- Monitor the deployment logs
- Once deployed, you'll get a URL like: `https://shl-assessment-agent.onrender.com`

## Testing Deployed API

### Health Check
```bash
curl https://shl-assessment-agent.onrender.com/health
```

### Interactive API Docs
Visit: `https://shl-assessment-agent.onrender.com/docs`

### Test Chat Endpoint
```bash
curl -X POST https://shl-assessment-agent.onrender.com/chat \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "I need an assessment for a software engineering role"}
    ]
  }'
```

## Important Notes

⚠️ **Free Tier Limitations:**
- Services spin down after 15 minutes of inactivity
- May take 30+ seconds to wake up
- Performance may be limited

✅ **Best Practices:**
- Use the Pro plan for production workloads
- Monitor logs in Render dashboard
- Set up alerts for deployment failures
- Keep your API key secure (use environment variables only)

## Troubleshooting

### Build Fails
- Check the build logs in Render dashboard
- Ensure all dependencies in `requirements.txt` are correct
- Verify Python version is 3.11+

### API Returns 500 Errors
- Check logs in Render dashboard
- Verify GEMINI_API_KEY is correctly set
- Ensure `.env` file is not included in git (it's in .gitignore)

### Cold Start Issues
- Free tier services take longer to start
- Consider upgrading to Pro plan for consistent performance

## Updating After Deployment

1. Make changes locally
2. Push to GitHub:
   ```bash
   git add .
   git commit -m "Your changes"
   git push origin main
   ```
3. Render automatically deploys from GitHub (if auto-deploy is enabled)

## Useful Render Dashboard Features
- **Logs**: Real-time application logs
- **Metrics**: CPU, memory, request statistics
- **Events**: Deployment history and status
- **Settings**: Manage environment variables and redeploy
