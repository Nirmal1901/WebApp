#!/bin/bash
# =======================================================
#   NuOps Demo Script
#   Run these commands in order during your demo
# =======================================================

# ── STEP 1: Initial push (CI passes) ──────────────────
# This shows a healthy green pipeline first
echo "=== STEP 1: Push working code (CI will PASS) ==="
echo ""
echo "Run these commands:"
echo ""
echo "  git init"
echo "  git remote add origin https://github.com/YOUR_USERNAME/nuops-demo"
echo "  git add ."
echo "  git commit -m 'feat: initial user management API'"
echo "  git push -u origin main"
echo ""
echo "→ Go to GitHub Actions tab - show green ✅ pipeline"
echo "→ Wait ~30 seconds for pipeline to complete"
echo ""
read -p "Press Enter when CI is green and you're ready to break it..."

# ── STEP 2: Break it ──────────────────────────────────
echo ""
echo "=== STEP 2: Developer pushes a 'quick fix' that breaks CI ==="
echo ""
echo "  cp app/main_broken.py app/main.py"
echo "  git add app/main.py"
echo "  git commit -m 'fix: optimize discount calculation and add promote endpoint'"
echo "  git push"
echo ""
echo "→ Show GitHub Actions tab - pipeline running..."
echo "→ It will turn RED ❌ in ~30 seconds"
echo "→ Meanwhile explain: 'Normally a dev would spend 20 min reading logs'"
echo ""
read -p "Press Enter when CI shows red..."

# ── STEP 3: NuOps fires ───────────────────────────────
echo ""
echo "=== STEP 3: NuOps detects the failure ==="
echo ""
echo "→ Show your terminal running server.py"
echo "→ They will see:"
echo "   INFO Received event: [workflow_run]"
echo "   INFO CI failure detected! Spawning NuOps analysis..."
echo "   INFO Running NuOps agent..."
echo ""
echo "→ Switch to GitHub Issues tab"
echo "→ Refresh in ~30 seconds..."
echo ""
read -p "Press Enter when GitHub Issue appears..."

# ── STEP 4: Show the issue ────────────────────────────
echo ""
echo "=== STEP 4: Show the GitHub Issue NuOps created ==="
echo ""
echo "The issue should contain:"
echo ""
echo "  ### Root Cause"
echo "  3 bugs introduced in app/main.py:"
echo "  1. ZeroDivisionError in calculate_discount() when discount=100"
echo "  2. Missing APP_SECRET_KEY environment variable (KeyError at startup)"
echo "  3. Test assertions fail due to changed behavior"
echo ""
echo "  ### Fix Required"
echo "  [exact code fixes]"
echo ""
echo "→ Point out: NuOps read the logs, read the code, understood all 3 bugs"
echo "→ 'A dev would take 20 min. NuOps took 30 seconds.'"
echo ""

echo "=== DEMO COMPLETE ==="
