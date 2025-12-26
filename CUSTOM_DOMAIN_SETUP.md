# Custom Domain Setup Guide for opennursingcoreig.com

## Step 1: Configure DNS in IONOS (You need to do this)

Log in to your IONOS account and add these DNS records:

### A Records (Required - Add all 4)
| Type | Host/Name | Points To | TTL |
|------|-----------|-----------|-----|
| A | @ | 185.199.108.153 | 3600 |
| A | @ | 185.199.109.153 | 3600 |
| A | @ | 185.199.110.153 | 3600 |
| A | @ | 185.199.111.153 | 3600 |

### AAAA Records (Optional - for IPv6)
| Type | Host/Name | Points To | TTL |
|------|-----------|-----------|-----|
| AAAA | @ | 2606:50c0:8000::153 | 3600 |
| AAAA | @ | 2606:50c0:8001::153 | 3600 |
| AAAA | @ | 2606:50c0:8002::153 | 3600 |
| AAAA | @ | 2606:50c0:8003::153 | 3600 |

### CNAME Record (Recommended - for www subdomain)
| Type | Host/Name | Points To | TTL |
|------|-----------|-----------|-----|
| CNAME | www | clinyqai.github.io | 3600 |

**Note**: In IONOS, `@` means the root domain (opennursingcoreig.com). Some interfaces might use a blank field or "root" instead.

## Step 2: Add CNAME File to Repository (I'll do this)

Create a file named `CNAME` in the repository root with the domain name.

## Step 3: Configure GitHub Pages (I'll do this)

Set the custom domain in GitHub Pages settings.

## DNS Propagation

- DNS changes can take 24-48 hours to fully propagate
- You can check status at: https://www.whatsmydns.net/#A/opennursingcoreig.com
- HTTPS certificate will auto-provision after DNS propagates (takes ~24 hours)

## After Setup

Your IG will be available at:
- https://opennursingcoreig.com (primary)
- https://www.opennursingcoreig.com (redirects to primary)
- Old URL (https://clinyqai.github.io/open-nursing-core-ig/) will redirect automatically
