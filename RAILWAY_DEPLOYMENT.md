# 🚂 Railway Deployment Guide

Complete guide to deploy your Diet Recommendation System on Railway.

---

## 🎯 What You'll Deploy

Your complete application including:
- ✅ Streamlit Frontend
- ✅ FastAPI Backend  
- ✅ 500K+ Recipe Database
- ✅ ML Recommendation Engine

**All in one deployment!**

---

## 📋 Prerequisites

- ✅ GitHub account (you have this)
- ✅ Code pushed to GitHub (done!)
- ✅ Railway account (free - we'll create this)

---

## 🚀 Step-by-Step Deployment

### Step 1: Create Railway Account

1. Go to: **https://railway.app**
2. Click **"Login"** or **"Start a New Project"**
3. Click **"Login with GitHub"**
4. Authorize Railway to access your GitHub

### Step 2: Create New Project

1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Choose: **`Saiteja1718/diet-recommendation-system`**
4. Railway will detect your Python app automatically

### Step 3: Configure Your App

Railway will auto-detect settings, but verify:

#### Environment Variables (Optional):
- Click on your service
- Go to **"Variables"** tab
- Add if needed:
  ```
  PYTHON_VERSION=3.10
  PORT=8501
  ```

#### Build Settings:
Railway auto-detects from your `Procfile`:
```
Start Command: streamlit run Streamlit_Frontend/Hello.py --server.port=$PORT --server.address=0.0.0.0
```

### Step 4: Deploy!

1. Railway will automatically start building
2. Wait 3-5 minutes for:
   - ✅ Installing dependencies
   - ✅ Loading dataset
   - ✅ Starting application

3. Watch the build logs in real-time

### Step 5: Get Your URL

1. Once deployed, click **"Settings"**
2. Scroll to **"Domains"**
3. Click **"Generate Domain"**
4. Your app will be live at:
   ```
   https://[your-app-name].up.railway.app
   ```

---

## ✅ Verification

Test your deployed app:

1. **Open your Railway URL**
2. **Test Features**:
   - ✅ Welcome page loads
   - ✅ Diet Recommendation works
   - ✅ Custom Search works
   - ✅ Meal Planner works
   - ✅ Chat assistant responds

---

## 🔧 Configuration Files Added

I've added these files for Railway:

### 1. `railway.json`
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "numReplicas": 1,
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

### 2. `Procfile`
```
web: streamlit run Streamlit_Frontend/Hello.py --server.port=$PORT --server.address=0.0.0.0
```

### 3. `requirements.txt` (Updated)
All dependencies in one file for Railway.

---

## 💰 Pricing

**Railway Free Tier:**
- ✅ $5 free credit per month
- ✅ Enough for development/testing
- ✅ No credit card required to start
- ✅ Automatic sleep after inactivity (saves credits)

**Your app usage:**
- ~$0.01-0.05 per hour when active
- Sleeps when not in use
- Should fit in free tier for personal use

---

## 🔄 Auto-Deployment

**Already configured!**

Every time you push to GitHub:
1. Railway detects the change
2. Automatically rebuilds
3. Deploys new version
4. Zero downtime deployment

```bash
# Make changes
git add .
git commit -m "Update feature"
git push origin main

# Railway auto-deploys! 🚀
```

---

## 📊 Monitoring

### View Logs:
1. Click on your service in Railway
2. Go to **"Deployments"** tab
3. Click on latest deployment
4. View real-time logs

### Check Metrics:
1. Go to **"Metrics"** tab
2. See:
   - CPU usage
   - Memory usage
   - Network traffic
   - Request count

---

## 🐛 Troubleshooting

### Build Fails

**Issue**: Dependencies not installing
```bash
# Solution: Check requirements.txt
# Make sure all packages are listed with versions
```

**Issue**: Python version mismatch
```bash
# Solution: Railway uses Python 3.10 by default
# Your app is compatible ✅
```

### App Crashes

**Issue**: Port binding error
```bash
# Solution: Already configured in Procfile
# Uses $PORT environment variable ✅
```

**Issue**: Out of memory
```bash
# Solution: Railway provides 512MB-1GB RAM
# Your app should fit, but monitor usage
```

### Slow Performance

**Issue**: App is slow to respond
```bash
# Solution: 
# 1. Check if app is sleeping (first request wakes it)
# 2. Upgrade to paid plan for always-on
# 3. Optimize code/reduce dataset size
```

---

## 🎨 Custom Domain (Optional)

### Add Your Own Domain:

1. Go to **Settings** → **Domains**
2. Click **"Custom Domain"**
3. Enter your domain: `yourdomain.com`
4. Update DNS records:
   ```
   Type: CNAME
   Name: @
   Value: [provided by Railway]
   ```
5. Wait for DNS propagation (5-30 minutes)

---

## 🔐 Environment Secrets

### Add Sensitive Data:

1. Go to **Variables** tab
2. Click **"New Variable"**
3. Add key-value pairs:
   ```
   API_KEY=your_secret_key
   DATABASE_URL=your_db_url
   ```
4. Access in code:
   ```python
   import os
   api_key = os.getenv('API_KEY')
   ```

---

## 📈 Scaling (If Needed)

### Upgrade Plan:

1. Go to **Settings**
2. Click **"Change Plan"**
3. Choose:
   - **Hobby**: $5/month (always-on, more resources)
   - **Pro**: $20/month (high performance)

### Horizontal Scaling:

1. Edit `railway.json`
2. Change `numReplicas`:
   ```json
   "deploy": {
     "numReplicas": 2  // Run 2 instances
   }
   ```

---

## 🎉 Success Checklist

After deployment:

- [ ] App is live and accessible
- [ ] All features work correctly
- [ ] Auto-deployment is enabled
- [ ] Monitoring is set up
- [ ] Domain configured (optional)
- [ ] README updated with live URL
- [ ] Shared with friends/portfolio

---

## 📝 Update README

Add your live URL to README.md:

```markdown
## 🌐 Live Demo

**Try it now:** https://[your-app].up.railway.app

Deployed on Railway 🚂
```

---

## 🆘 Need Help?

- **Railway Docs**: https://docs.railway.app
- **Railway Discord**: https://discord.gg/railway
- **Railway Status**: https://status.railway.app

---

## 🎊 You're Done!

Your Diet Recommendation System is now live on Railway!

**Next Steps:**
1. Share your live URL
2. Add to your portfolio
3. Get feedback from users
4. Keep improving!

**Enjoy your deployed app!** 🚀🎉
