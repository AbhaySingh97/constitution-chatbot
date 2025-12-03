# Constitution Chatbot - Railway Deployment Guide

## 🚂 Deploy to Railway in 5 Minutes

Railway is the easiest platform to deploy your Constitution Chatbot. Follow these steps:

---

## Step 1: Initialize Git Repository

```bash
cd "c:\Users\User\OneDrive\Desktop\FULL STACK\NLM MODEL\constitution-chatbot"
git init
git add .
git commit -m "Constitution Chatbot - Railway deployment"
```

---

## Step 2: Create GitHub Repository

### Option A: Using GitHub Desktop (Easiest)
1. Download and install [GitHub Desktop](https://desktop.github.com/)
2. Open GitHub Desktop
3. File → Add Local Repository
4. Select: `c:\Users\User\OneDrive\Desktop\FULL STACK\NLM MODEL\constitution-chatbot`
5. Click "Publish repository"
6. Name: `constitution-chatbot`
7. Click "Publish repository"

### Option B: Using GitHub Website
1. Go to [github.com](https://github.com)
2. Click "+" → "New repository"
3. Name: `constitution-chatbot`
4. Description: "AI-powered Indian Constitution chatbot with 102 articles, legal procedures, and landmark cases"
5. Click "Create repository"
6. Follow the instructions to push existing repository:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/constitution-chatbot.git
   git branch -M main
   git push -u origin main
   ```

---

## Step 3: Deploy on Railway

### 3.1 Sign Up for Railway
1. Go to [railway.app](https://railway.app)
2. Click "Login" or "Start a New Project"
3. Sign up with GitHub (recommended)
4. Authorize Railway to access your GitHub

### 3.2 Create New Project
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose `constitution-chatbot` repository
4. Railway will automatically detect:
   - ✅ Python project
   - ✅ requirements.txt
   - ✅ Procfile
   - ✅ Railway configuration

### 3.3 Configure (Auto-detected)
Railway automatically configures:
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app` (from Procfile)
- **Port**: Automatically set via $PORT environment variable
- **Python Version**: 3.11 (from runtime.txt)

### 3.4 Deploy
1. Click "Deploy"
2. Wait 2-3 minutes for build and deployment
3. Railway will show build logs in real-time

### 3.5 Get Your URL
1. Once deployed, click "Settings"
2. Under "Domains", click "Generate Domain"
3. Your app will be live at: `https://constitution-chatbot-production.up.railway.app`

---

## Step 4: Verify Deployment

1. Open your Railway URL
2. Test these queries:
   - "What is Article 21?"
   - "How to file PIL?"
   - "Kesavananda Bharati case"
   - "Article 370"

---

## Railway Features

### ✅ What You Get (Free Tier)
- **$5 free credit per month** (500 hours of usage)
- **Auto-deploy** on every git push
- **Custom domains** support
- **Environment variables** management
- **Real-time logs** and monitoring
- **Automatic HTTPS**

### 📊 Resource Limits (Free Tier)
- 512 MB RAM
- 1 GB Disk
- Shared CPU
- Perfect for this chatbot!

---

## Troubleshooting

### Build Fails
**Check:**
- All files committed to git
- requirements.txt is present
- Procfile is present

**Solution:**
```bash
git add .
git commit -m "Fix deployment"
git push
```

### App Crashes
**Check Railway Logs:**
1. Go to Railway dashboard
2. Click on your project
3. Click "View Logs"
4. Look for errors

**Common fixes:**
- Verify PORT environment variable is used
- Check gunicorn is in requirements.txt

### Slow First Load
- Railway free tier sleeps after inactivity
- First request takes 10-30 seconds
- Subsequent requests are fast

---

## Post-Deployment

### Update Your App
```bash
# Make changes to your code
git add .
git commit -m "Update: description of changes"
git push
```
Railway automatically redeploys!

### Add Custom Domain
1. Railway Dashboard → Settings → Domains
2. Click "Custom Domain"
3. Enter your domain
4. Update DNS records as shown

### Monitor Usage
1. Railway Dashboard → Usage
2. Check remaining free credits
3. Upgrade if needed ($5/month for more resources)

---

## Environment Variables (Optional)

If you need to add environment variables:

1. Railway Dashboard → Variables
2. Add:
   - `FLASK_ENV=production` (already set by default)
   - Any other custom variables

---

## Your Chatbot Stats

- **102 Constitutional Articles**
- **4 Legal Procedures**
- **10 Landmark Supreme Court Cases**
- **116 Total Entries**
- **Production-ready with Gunicorn**
- **Auto-scaling on Railway**

---

## Need Help?

- Railway Docs: [docs.railway.app](https://docs.railway.app)
- Railway Discord: [discord.gg/railway](https://discord.gg/railway)
- Check logs in Railway dashboard

---

**Ready to deploy? Follow Step 1 above! 🚀**
