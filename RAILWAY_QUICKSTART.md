# 🚂 Railway Deployment - Quick Start

## ✅ Your Project is Railway-Ready!

All necessary files have been created and configured:
- ✅ `requirements.txt` - Dependencies
- ✅ `Procfile` - Start command
- ✅ `runtime.txt` - Python version
- ✅ `railway.json` - Railway config
- ✅ `railway.toml` - Alternative config
- ✅ `.gitignore` - Exclude unnecessary files
- ✅ Git repository initialized
- ✅ Initial commit created

## 🎯 Next Steps (Choose One):

### Option 1: Deploy via GitHub (Recommended)

**Step 1: Create GitHub Repository**

Using GitHub Desktop (Easiest):
1. Download [GitHub Desktop](https://desktop.github.com/)
2. Install and login
3. File → Add Local Repository
4. Browse to your `constitution-chatbot` folder
5. Click "Publish repository"
6. Name: `constitution-chatbot`
7. Make it Public or Private
8. Click "Publish repository"

**Step 2: Deploy on Railway**
1. Go to [railway.app](https://railway.app)
2. Login with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose `constitution-chatbot`
6. Railway auto-detects everything
7. Click "Deploy"
8. Wait 2-3 minutes
9. Click "Settings" → "Generate Domain"
10. Your app is live! 🎉

### Option 2: Deploy via Railway CLI

**Step 1: Install Railway CLI**
```bash
npm install -g @railway/cli
```

**Step 2: Login**
```bash
railway login
```

**Step 3: Initialize and Deploy**
```bash
cd constitution-chatbot
railway init
railway up
```

**Step 4: Get URL**
```bash
railway domain
```

---

## 📊 What's Deployed

- **102 Constitutional Articles**
- **4 Legal Procedures** (PIL, Writs, Amendment, Impeachment)
- **10 Landmark Cases** (Kesavananda Bharati, Puttaswamy, etc.)
- **Enhanced Search** with keyword matching
- **Production-ready** with Gunicorn

---

## 🔍 Test Queries After Deployment

1. "What is Article 21?"
2. "Article 370"
3. "How to file PIL?"
4. "Kesavananda Bharati case"
5. "Right to Privacy"
6. "Tell me about fundamental rights"

---

## 💡 Tips

- **Free Tier**: $5 credit/month (500 hours)
- **Auto-deploy**: Push to GitHub = Auto redeploy
- **Logs**: View in Railway dashboard
- **Custom Domain**: Add in Railway settings

---

## 🆘 Need Help?

See `RAILWAY_DEPLOY.md` for detailed step-by-step guide.

---

**Ready to go live? Follow Option 1 above! 🚀**
