# 🚀 Deployment Guide - Diet Recommendation System

This guide covers deploying your Diet Recommendation System to cloud platforms.

---

## ⚠️ Important: Vercel Limitations for Python

**Vercel is optimized for Node.js/Next.js** and has limited Python support. For this Python project, I recommend:

1. **Streamlit Cloud** (Frontend) - FREE ✅ **RECOMMENDED**
2. **Railway/Render** (Backend) - FREE tier available

---

## 🌟 Recommended: Streamlit Cloud

### Deploy to Streamlit Cloud (5 minutes)

**Best for:** Your Streamlit frontend (FREE, unlimited public apps)

#### Steps:

1. **Your code is already on GitHub** ✅
   ```
   https://github.com/Saiteja1718/diet-recommendation-system
   ```

2. **Go to Streamlit Cloud**
   - Visit: https://streamlit.io/cloud
   - Click "Sign in with GitHub"

3. **Deploy Your App**
   - Click "New app"
   - Repository: `Saiteja1718/diet-recommendation-system`
   - Branch: `main`
   - Main file path: `Streamlit_Frontend/Hello.py`
   - Click "Deploy"

4. **Done!** Your app will be live at:
   ```
   https://[your-app-name].streamlit.app
   ```

#### Features:
- ✅ FREE for public apps
- ✅ Auto-deploy on git push
- ✅ Built specifically for Streamlit
- ✅ No configuration needed

---

## 🔧 Deploy Backend (Railway - Recommended)

### Railway Setup (10 minutes)

1. **Sign up**: https://railway.app (use GitHub)

2. **New Project** → "Deploy from GitHub repo"

3. **Select**: `Saiteja1718/diet-recommendation-system`

4. **Configure**:
   - Root directory: `FastAPI_Backend`
   - Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

5. **Deploy** - Get URL: `https://[your-api].railway.app`

6. **Update Frontend**:
   - Edit `Generate_Recommendations.py`
   - Change API URL to your Railway URL

---

## 📋 Quick Start Commands

### Commit deployment files:

```bash
git add .streamlit/config.toml runtime.txt DEPLOYMENT.md
git commit -m "Add deployment configuration"
git push origin main
```

---

## ✅ Post-Deployment

1. Test your live app
2. Update README with live URL
3. Share your project!

**Need help?** Check the full DEPLOYMENT.md guide in your repository.
