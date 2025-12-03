# Constitution Chatbot - Deployment Guide

## Quick Deployment Options

### Option 1: Deploy to Render (Recommended - Free Tier Available)

1. **Create GitHub Repository**
   ```bash
   cd "c:\Users\User\OneDrive\Desktop\FULL STACK\NLM MODEL\constitution-chatbot"
   git init
   git add .
   git commit -m "Initial commit - Constitution Chatbot"
   ```

2. **Push to GitHub**
   - Create a new repository on GitHub
   - Follow GitHub's instructions to push your code

3. **Deploy on Render**
   - Go to [render.com](https://render.com)
   - Sign up/Login with GitHub
   - Click "New +" → "Web Service"
   - Connect your repository
   - Configure:
     - **Name**: constitution-chatbot
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
     - **Instance Type**: Free
   - Click "Create Web Service"
   - Wait 2-3 minutes for deployment
   - Your app will be live at: `https://constitution-chatbot.onrender.com`

### Option 2: Deploy to Railway (Free Tier Available)

1. **Create GitHub Repository** (same as above)

2. **Deploy on Railway**
   - Go to [railway.app](https://railway.app)
   - Sign up/Login with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Railway auto-detects Python and uses Procfile
   - Click "Deploy"
   - Your app will be live in 2-3 minutes

### Option 3: Deploy to Vercel (Serverless)

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Create vercel.json**
   Already created in your project

3. **Deploy**
   ```bash
   cd "c:\Users\User\OneDrive\Desktop\FULL STACK\NLM MODEL\constitution-chatbot"
   vercel
   ```
   - Follow the prompts
   - Your app will be live at: `https://your-project.vercel.app`

### Option 4: Deploy to Heroku

1. **Install Heroku CLI**
   Download from [heroku.com](https://devcenter.heroku.com/articles/heroku-cli)

2. **Login and Create App**
   ```bash
   heroku login
   cd "c:\Users\User\OneDrive\Desktop\FULL STACK\NLM MODEL\constitution-chatbot"
   heroku create constitution-chatbot-india
   ```

3. **Deploy**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push heroku main
   ```

4. **Open App**
   ```bash
   heroku open
   ```

## Testing Before Deployment

1. **Test Production Mode Locally**
   ```bash
   # Install gunicorn
   pip install gunicorn
   
   # Run with gunicorn
   gunicorn app:app
   ```
   
   Open: http://localhost:8000

2. **Verify All Features**
   - Test article queries
   - Test procedure queries
   - Test landmark case queries
   - Test quick replies
   - Check mobile responsiveness

## Post-Deployment Checklist

- [ ] Test all quick reply questions
- [ ] Verify Article 370 shows full details
- [ ] Test PIL procedure
- [ ] Test landmark cases (Kesavananda Bharati, Puttaswamy, etc.)
- [ ] Check mobile responsiveness
- [ ] Test search functionality
- [ ] Verify all 102 articles are accessible

## Environment Variables (Optional)

If you want to add environment-specific settings:

```bash
# For development
FLASK_ENV=development

# For production (automatically set by hosting platforms)
FLASK_ENV=production
PORT=5000
```

## Monitoring & Maintenance

### Render
- View logs in Render dashboard
- Auto-deploys on git push
- Free tier: sleeps after 15 min inactivity

### Railway
- View logs in Railway dashboard
- Auto-deploys on git push
- Free tier: 500 hours/month

### Heroku
- View logs: `heroku logs --tail`
- Auto-deploys on git push
- Free tier: sleeps after 30 min inactivity

## Custom Domain (Optional)

After deployment, you can add a custom domain:

1. **Render**: Settings → Custom Domain
2. **Railway**: Settings → Domains
3. **Heroku**: Settings → Domains
4. **Vercel**: Settings → Domains

## Troubleshooting

### Build Fails
- Check `requirements.txt` has all dependencies
- Verify Python version in `runtime.txt`

### App Crashes
- Check logs for errors
- Verify `gunicorn` is in requirements.txt
- Check PORT environment variable

### Slow Response
- First request after sleep takes 10-30 seconds (free tier)
- Consider upgrading to paid tier for always-on

## Need Help?

- Check deployment platform documentation
- Review error logs
- Test locally first with `gunicorn app:app`

---

**Your chatbot is production-ready! Choose your preferred platform and deploy! 🚀**
