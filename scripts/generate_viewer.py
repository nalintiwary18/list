import json
import os
import re

def generate_html_viewer():
    json_path = os.path.join(os.path.dirname(__file__), "..", "companies_data.json")
    with open(json_path, "r", encoding="utf-8") as f:
        companies = json.load(f)

    audit_path = os.path.join(os.path.dirname(__file__), "..", "company_link_audit.json")
    with open(audit_path, "r", encoding="utf-8") as f:
        link_audit = json.load(f)
    link_audit_by_id = {str(item["id"]): item for item in link_audit["records"]}
    
    engine_path = os.path.join(os.path.dirname(__file__), "outreach_engine.js")
    with open(engine_path, "r", encoding="utf-8") as f:
        engine_js = f.read()

    for company in companies:
        company["link_audit"] = link_audit_by_id.get(str(company["id"]), {})
        
    total_count = len(companies)
    tier_a_count = sum(1 for c in companies if c.get("tier") == "Tier A")
    tier_b_count = sum(1 for c in companies if c.get("tier") == "Tier B")
    tier_c_count = sum(1 for c in companies if c.get("tier") == "Tier C")
    delhi_count = sum(1 for c in companies if any(loc in (c.get("work_model_location") or "").lower() for loc in ["delhi", "noida", "gurgaon"]))
    remote_count = sum(1 for c in companies if "remote" in (c.get("work_model_location") or "").lower())
    
    companies_json = json.dumps(companies, ensure_ascii=False)

    html_content = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">
    <meta name="theme-color" content="#0a0a0a" media="(prefers-color-scheme: dark)">
    <meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="AI Prospects">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🎯</text></svg>">
    <title>Target Startups: {total_count} Funded AI Startups (&lt;100 Employees) | Kumar Nalin</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root, [data-theme="dark"] {{
            --bg-page: #0a0a0a;
            --bg-surface: #121212;
            --bg-surface-elevated: #1a1a1a;
            --bg-surface-hover: #242424;
            --bg-subtle: #2b2b2b;
            --bg-input: #0f0f0f;
            
            --border-subtle: #242424;
            --border-medium: #383838;
            --border-strong: #525252;
            --border-focus: #ffffff;
            
            --text-primary: #f5f5f5;
            --text-secondary: #a3a3a3;
            --text-muted: #737373;
            --text-inverted: #0a0a0a;
            
            --btn-primary-bg: #f5f5f5;
            --btn-primary-text: #0a0a0a;
            --btn-primary-hover: #ffffff;
            
            --btn-secondary-bg: #1a1a1a;
            --btn-secondary-text: #e5e5e5;
            --btn-secondary-border: #383838;
            --btn-secondary-hover: #242424;
            
            --badge-bg: #1a1a1a;
            --badge-text: #d4d4d4;
            --badge-border: #2e2e2e;
            
            --badge-active-bg: #f5f5f5;
            --badge-active-text: #0a0a0a;
            --badge-active-border: #f5f5f5;
            
            --table-header-bg: #121212;
            --table-row-hover: #171717;
            --table-row-border: #1f1f1f;
            
            --card-shadow: 0 1px 3px rgba(0, 0, 0, 0.5);
            --modal-overlay: rgba(0, 0, 0, 0.85);
            --modal-bg: #121212;
            --toast-bg: #f5f5f5;
            --toast-text: #0a0a0a;
        }}

        [data-theme="light"] {{
            --bg-page: #f5f5f5;
            --bg-surface: #ffffff;
            --bg-surface-elevated: #ffffff;
            --bg-surface-hover: #eeeeee;
            --bg-subtle: #e5e5e5;
            --bg-input: #ffffff;
            
            --border-subtle: #e5e5e5;
            --border-medium: #d4d4d4;
            --border-strong: #8a8a8a;
            --border-focus: #0a0a0a;
            
            --text-primary: #0a0a0a;
            --text-secondary: #525252;
            --text-muted: #737373;
            --text-inverted: #f5f5f5;
            
            --btn-primary-bg: #0a0a0a;
            --btn-primary-text: #ffffff;
            --btn-primary-hover: #262626;
            
            --btn-secondary-bg: #ffffff;
            --btn-secondary-text: #171717;
            --btn-secondary-border: #d4d4d4;
            --btn-secondary-hover: #eeeeee;
            
            --badge-bg: #f0f0f0;
            --badge-text: #171717;
            --badge-border: #d4d4d4;
            
            --badge-active-bg: #0a0a0a;
            --badge-active-text: #ffffff;
            --badge-active-border: #0a0a0a;
            
            --table-header-bg: #f5f5f5;
            --table-row-hover: #fafafa;
            --table-row-border: #ebebeb;
            
            --card-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
            --modal-overlay: rgba(0, 0, 0, 0.45);
            --modal-bg: #ffffff;
            --toast-bg: #0a0a0a;
            --toast-text: #ffffff;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            background-color: var(--bg-page);
            color: var(--text-primary);
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            line-height: 1.5;
            min-height: 100vh;
            padding: 24px;
            padding-top: max(16px, env(safe-area-inset-top));
            padding-bottom: max(24px, env(safe-area-inset-bottom));
            padding-left: max(16px, env(safe-area-inset-left));
            padding-right: max(16px, env(safe-area-inset-right));
            transition: background-color 0.2s ease, color 0.2s ease;
            -webkit-font-smoothing: antialiased;
        }}

        .container {{
            max-width: 1560px;
            margin: 0 auto;
        }}

        /* Header */
        header {{
            margin-bottom: 24px;
            padding-bottom: 20px;
            border-bottom: 1px solid var(--border-subtle);
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 16px;
        }}

        .header-title h1 {{
            font-size: 26px;
            font-weight: 800;
            letter-spacing: -0.025em;
            color: var(--text-primary);
        }}

        .header-title p {{
            color: var(--text-secondary);
            font-size: 13px;
            margin-top: 3px;
        }}

        .header-actions {{
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            gap: 8px;
        }}

        .action-btn {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: var(--bg-surface-elevated);
            border: 1px solid var(--border-medium);
            color: var(--text-primary);
            padding: 7px 12px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.15s, border-color 0.15s, color 0.15s;
            text-decoration: none;
            font-family: inherit;
        }}

        .action-btn:hover {{
            background: var(--bg-surface-hover);
            border-color: var(--border-strong);
        }}

        .action-btn-primary {{
            background: var(--text-primary);
            color: var(--text-inverted);
            border-color: var(--text-primary);
            font-weight: 700;
        }}

        .action-btn-primary:hover {{
            background: var(--border-strong);
            color: var(--text-primary);
            border-color: var(--border-strong);
        }}

        .btn-danger {{
            background: var(--bg-surface-elevated);
            border: 1px solid var(--border-medium);
            color: var(--text-muted);
        }}

        .btn-danger:hover {{
            border-color: var(--border-focus);
            color: var(--text-primary);
            background: var(--bg-subtle);
        }}

        .theme-toggle-btn {{
            display: inline-flex;
            align-items: center;
            gap: 7px;
            background: var(--bg-surface-elevated);
            border: 1px solid var(--border-medium);
            color: var(--text-primary);
            padding: 7px 13px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.15s, border-color 0.15s;
        }}

        .theme-toggle-btn:hover {{
            background: var(--bg-surface-hover);
            border-color: var(--border-strong);
        }}

        .theme-icon {{
            display: inline-flex;
            align-items: center;
        }}

        .header-badge {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: var(--bg-surface-elevated);
            color: var(--text-primary);
            padding: 7px 13px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 600;
            border: 1px solid var(--border-medium);
            font-family: 'JetBrains Mono', monospace;
        }}

        .storage-status-btn {{
            display: inline-flex;
            align-items: center;
            gap: 7px;
            background: var(--bg-surface-elevated);
            color: var(--text-primary);
            padding: 7px 12px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 600;
            border: 1px solid var(--border-medium);
            cursor: pointer;
            transition: background 0.15s, border-color 0.15s;
            font-family: inherit;
        }}

        .storage-status-btn:hover {{
            background: var(--bg-surface-hover);
            border-color: var(--border-strong);
        }}

        .storage-dot {{
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: #10b981;
            display: inline-block;
            transition: transform 0.2s;
        }}

        [data-theme="dark"] .storage-dot {{
            background: #34d399;
        }}

        [data-theme="light"] .storage-dot {{
            background: #059669;
        }}

        .storage-dot.saved {{
            animation: storagePulse 1s ease-out;
        }}

        @keyframes storagePulse {{
            0% {{ transform: scale(1.8); }}
            50% {{ transform: scale(1.3); }}
            100% {{ transform: scale(1); }}
        }}

        /* Metrics Row */
        .metrics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
            gap: 14px;
            margin-bottom: 20px;
        }}

        .metric-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: 10px;
            padding: 16px 18px;
            box-shadow: var(--card-shadow);
            transition: border-color 0.15s, transform 0.15s;
        }}

        .metric-card:hover {{
            border-color: var(--border-medium);
            transform: translateY(-1px);
        }}

        .metric-label {{
            font-size: 11px;
            color: var(--text-muted);
            text-transform: uppercase;
            font-weight: 700;
            letter-spacing: 0.05em;
        }}

        .metric-val {{
            font-size: 26px;
            font-weight: 800;
            margin-top: 3px;
            color: var(--text-primary);
            font-family: 'JetBrains Mono', monospace;
        }}

        .metric-sub {{
            font-size: 12px;
            color: var(--text-secondary);
            margin-top: 2px;
        }}

        /* Controls Section */
        .controls-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: 12px;
            padding: 16px 18px;
            margin-bottom: 20px;
            box-shadow: var(--card-shadow);
            display: flex;
            flex-direction: column;
            gap: 14px;
        }}

        .controls-top {{
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            align-items: center;
            justify-content: space-between;
        }}

        .search-box {{
            flex: 1 1 360px;
            position: relative;
            display: flex;
            align-items: center;
        }}

        .search-box input {{
            width: 100%;
            background: var(--bg-input);
            border: 1px solid var(--border-medium);
            border-radius: 8px;
            padding: 9px 36px 9px 36px;
            color: var(--text-primary);
            font-size: 13px;
            font-family: inherit;
            outline: none;
            transition: border-color 0.15s, box-shadow 0.15s;
        }}

        .search-box input:focus {{
            border-color: var(--border-focus);
            box-shadow: 0 0 0 1px var(--border-focus);
        }}

        .search-icon {{
            position: absolute;
            left: 12px;
            color: var(--text-muted);
            display: inline-flex;
            align-items: center;
            pointer-events: none;
        }}

        .search-clear {{
            position: absolute;
            right: 10px;
            background: none;
            border: none;
            color: var(--text-muted);
            cursor: pointer;
            display: none;
            padding: 4px;
            align-items: center;
            border-radius: 4px;
        }}

        .search-clear:hover {{
            color: var(--text-primary);
        }}

        .selectors-group {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            align-items: center;
        }}

        .control-select {{
            background: var(--bg-input);
            border: 1px solid var(--border-medium);
            color: var(--text-primary);
            padding: 8px 12px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 500;
            outline: none;
            cursor: pointer;
            font-family: inherit;
            transition: border-color 0.15s;
        }}

        .control-select:focus {{
            border-color: var(--border-focus);
        }}

        /* View Toggle */
        .view-toggle {{
            display: inline-flex;
            background: var(--bg-surface-elevated);
            border: 1px solid var(--border-medium);
            border-radius: 8px;
            padding: 2px;
            gap: 2px;
        }}

        .view-toggle-btn {{
            display: inline-flex;
            align-items: center;
            gap: 5px;
            background: transparent;
            border: none;
            color: var(--text-secondary);
            padding: 5px 9px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.15s ease;
            font-family: inherit;
        }}

        .view-toggle-btn:hover {{
            color: var(--text-primary);
        }}

        .view-toggle-btn.active {{
            background: var(--badge-active-bg);
            color: var(--badge-active-text);
        }}

        /* More Actions Dropdown */
        .more-actions-wrap {{
            position: relative;
            display: inline-block;
        }}

        .more-actions-dropdown {{
            position: absolute;
            top: calc(100% + 6px);
            right: 0;
            background: var(--bg-surface);
            border: 1px solid var(--border-medium);
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45);
            padding: 6px;
            min-width: 170px;
            z-index: 50;
            display: none;
            flex-direction: column;
            gap: 4px;
        }}

        .more-actions-dropdown.open {{
            display: flex;
        }}

        .more-action-item {{
            display: flex;
            align-items: center;
            gap: 8px;
            background: transparent;
            border: none;
            color: var(--text-primary);
            padding: 8px 10px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 500;
            width: 100%;
            text-align: left;
            cursor: pointer;
            font-family: inherit;
            transition: background 0.15s;
        }}

        .more-action-item:hover {{
            background: var(--bg-surface-hover);
        }}

        .controls-bottom {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            align-items: center;
            justify-content: space-between;
            padding-top: 6px;
            border-top: 1px solid var(--border-subtle);
        }}

        .filters-group {{
            display: flex;
            align-items: center;
            gap: 8px;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            white-space: nowrap;
            padding-bottom: 4px;
            scrollbar-width: none;
        }}

        .filters-group::-webkit-scrollbar {{
            display: none;
        }}

        .filter-btn {{
            flex-shrink: 0;
            background: var(--bg-surface-elevated);
            border: 1px solid var(--border-medium);
            color: var(--text-secondary);
            padding: 6px 12px;
            border-radius: 7px;
            font-size: 12px;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.15s, color 0.15s, border-color 0.15s;
        }}

        .filter-btn:hover {{
            color: var(--text-primary);
            border-color: var(--border-strong);
        }}

        .filter-btn.active {{
            background: var(--badge-active-bg);
            color: var(--badge-active-text);
            border-color: var(--badge-active-border);
        }}

        .count-showing {{
            font-size: 12px;
            color: var(--text-muted);
            font-family: 'JetBrains Mono', monospace;
        }}

        /* Table & Cards */
        .table-container {{
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: 12px;
            overflow: auto;
            max-height: calc(100vh - 320px);
            min-height: 400px;
            box-shadow: var(--card-shadow);
            position: relative;
        }}

        table {{
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            font-size: 13px;
            text-align: left;
        }}

        thead th {{
            position: sticky;
            top: 0;
            background: var(--table-header-bg);
            border-bottom: 2px solid var(--border-medium);
            padding: 12px 14px;
            color: var(--text-muted);
            font-weight: 700;
            text-transform: uppercase;
            font-size: 11px;
            letter-spacing: 0.05em;
            z-index: 10;
        }}

        tbody tr {{
            border-bottom: 1px solid var(--table-row-border);
            transition: background-color 0.1s ease;
        }}

        tbody tr:hover {{
            background-color: var(--table-row-hover);
        }}

        td {{
            padding: 12px 14px;
            vertical-align: top;
            border-bottom: 1px solid var(--table-row-border);
        }}

        .col-id {{
            color: var(--text-muted);
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            font-weight: 500;
            width: 44px;
        }}

        .company-name-cell {{
            min-width: 190px;
        }}

        .company-name-wrapper {{
            display: flex;
            align-items: center;
            gap: 6px;
            flex-wrap: wrap;
        }}

        .company-link {{
            color: var(--text-primary);
            text-decoration: none;
            font-weight: 700;
            font-size: 14px;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }}

        .company-link:hover {{
            text-decoration: underline;
        }}

        .company-title {{
            font-weight: 700;
            font-size: 14px;
        }}

        .badge {{
            display: inline-block;
            padding: 2px 7px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 600;
            background: var(--bg-surface-elevated);
            border: 1px solid var(--border-medium);
            color: var(--text-secondary);
        }}

        .badge-tier-a {{
            background: var(--text-primary);
            color: var(--text-inverted);
            border-color: var(--text-primary);
            font-weight: 800;
            letter-spacing: 0.03em;
        }}

        .badge-tier-b {{
            background: var(--bg-subtle);
            color: var(--text-primary);
            border-color: var(--border-strong);
            font-weight: 700;
        }}

        .badge-tier-c {{
            background: var(--bg-surface-elevated);
            color: var(--text-muted);
            border-color: var(--border-subtle);
        }}

        .badge-score {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 10px;
            border-color: var(--border-medium);
            color: var(--text-secondary);
        }}

        .audit-label {{
            display: block;
            margin-top: 4px;
            color: var(--text-muted);
            font-size: 11px;
            line-height: 1.35;
        }}

        .date-sub {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 10px;
            margin-top: 3px;
        }}

        .audit-badge {{
            display: inline-block;
            margin-top: 5px;
            padding: 2px 7px;
            border-radius: 5px;
            font-size: 10px;
            font-family: 'JetBrains Mono', monospace;
            background: var(--bg-surface-elevated);
            color: var(--text-secondary);
            border: 1px solid var(--border-medium);
        }}

        .audit-badge.badge-alert {{
            border-color: var(--border-strong);
            color: var(--text-primary);
            font-weight: 700;
        }}

        .badge-sector {{
            max-width: 170px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            display: inline-block;
            font-size: 11px;
        }}

        .badge-size {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 10px;
            color: var(--text-muted);
        }}

        .badge-loc-delhi {{
            border: 1px solid var(--border-strong);
            background: var(--bg-subtle);
            color: var(--text-primary);
            font-weight: 600;
        }}

        .badge-loc-remote {{
            border: 1px solid var(--border-subtle);
            color: var(--text-secondary);
        }}

        .funding-cell {{
            font-size: 12px;
            color: var(--text-secondary);
            min-width: 160px;
            line-height: 1.4;
        }}

        .funding-stage {{
            font-weight: 600;
            color: var(--text-primary);
        }}

        .hook-cell {{
            color: var(--text-secondary);
            font-size: 12px;
            max-width: 260px;
            line-height: 1.45;
        }}

        .hook-text {{
            display: -webkit-box;
            -webkit-line-clamp: 4;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}

        .actions-cell {{
            min-width: 190px;
        }}

        .action-stack {{
            display: flex;
            flex-direction: column;
            gap: 5px;
        }}

        .email-text {{
            font-size: 11px;
            font-family: 'JetBrains Mono', monospace;
            color: var(--text-muted);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            display: block;
            max-width: 190px;
        }}

        .email-verify {{
            display: flex;
            align-items: center;
            gap: 5px;
            color: var(--text-muted);
            font-size: 10px;
            cursor: pointer;
            user-select: none;
        }}

        .email-verify input {{
            cursor: pointer;
            accent-color: var(--border-focus);
        }}

        .btn-copy, .btn-link, .draft-btn {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 5px;
            padding: 5px 9px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.15s ease;
            text-decoration: none;
            font-family: inherit;
        }}

        .btn-copy {{
            background: var(--bg-surface-elevated);
            border: 1px solid var(--border-medium);
            color: var(--text-primary);
        }}

        .btn-copy:hover {{
            background: var(--bg-surface-hover);
            border-color: var(--border-strong);
        }}

        .btn-copy.btn-copied {{
            background: var(--badge-active-bg);
            color: var(--badge-active-text);
            border-color: var(--badge-active-border);
        }}

        .btn-link {{
            background: transparent;
            border: 1px solid var(--border-medium);
            color: var(--text-secondary);
        }}

        .btn-link:hover {{
            color: var(--text-primary);
            border-color: var(--border-strong);
            background: var(--bg-surface-elevated);
        }}

        .draft-btn {{
            background: var(--btn-primary-bg);
            color: var(--btn-primary-text);
            border: 1px solid var(--btn-primary-bg);
            padding: 6px 11px;
        }}

        .draft-btn:hover {{
            background: var(--btn-primary-hover);
            border-color: var(--btn-primary-hover);
        }}

        .status-cell {{
            min-width: 140px;
        }}

        .status-select {{
            width: 100%;
            background: var(--bg-input);
            border: 1px solid var(--border-medium);
            color: var(--text-primary);
            padding: 6px 8px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 500;
            outline: none;
            cursor: pointer;
            font-family: inherit;
            transition: border-color 0.15s;
        }}

        .status-select:focus {{
            border-color: var(--border-focus);
        }}

        /* Empty state */
        .empty-state-cell {{
            text-align: center;
            padding: 60px 20px !important;
        }}

        .empty-state {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 6px;
        }}

        .empty-state-title {{
            font-size: 16px;
            font-weight: 700;
            color: var(--text-primary);
        }}

        .empty-state-sub {{
            font-size: 13px;
            color: var(--text-muted);
        }}

        /* Modal */
        .modal {{
            display: none;
            position: fixed;
            inset: 0;
            z-index: 1000;
            padding: 24px;
            overflow-y: auto;
            background: var(--modal-overlay);
        }}

        .modal.open {{
            display: block;
        }}

        .modal-card {{
            max-width: 1060px;
            margin: 2vh auto;
            padding: 24px;
            background: var(--modal-bg);
            border: 1px solid var(--border-strong);
            border-radius: 14px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
        }}

        .modal-head {{
            display: flex;
            justify-content: space-between;
            gap: 16px;
            align-items: flex-start;
            margin-bottom: 16px;
            padding-bottom: 14px;
            border-bottom: 1px solid var(--border-subtle);
        }}

        .modal-head h2 {{
            font-size: 20px;
            font-weight: 800;
            color: var(--text-primary);
            letter-spacing: -0.02em;
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }}

        .modal-meta {{
            margin-top: 6px;
            color: var(--text-secondary);
            font-size: 12px;
            line-height: 1.5;
        }}

        .score-breakdown-row {{
            background: var(--bg-surface-elevated);
            padding: 8px 12px;
            border-radius: 7px;
            border: 1px solid var(--border-subtle);
            font-size: 11px;
            color: var(--text-secondary);
            margin-top: 8px;
            font-family: 'JetBrains Mono', monospace;
        }}

        .close-btn {{
            border: 1px solid var(--border-medium);
            background: var(--bg-surface-elevated);
            color: var(--text-secondary);
            width: 32px;
            height: 32px;
            border-radius: 8px;
            font-size: 18px;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            line-height: 1;
            transition: background 0.15s, color 0.15s;
        }}

        .close-btn:hover {{
            background: var(--bg-surface-hover);
            color: var(--text-primary);
            border-color: var(--border-strong);
        }}

        .engine-grid {{
            display: grid;
            grid-template-columns: minmax(320px, 0.95fr) minmax(380px, 1.05fr);
            gap: 20px;
        }}

        .engine-section {{
            padding: 18px;
            border: 1px solid var(--border-subtle);
            border-radius: 10px;
            background: var(--bg-surface);
        }}

        .engine-section h3 {{
            margin-bottom: 14px;
            font-weight: 700;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            font-size: 11px;
            color: var(--text-muted);
        }}

        .engine-field {{
            display: block;
            margin-bottom: 12px;
            color: var(--text-secondary);
            font-size: 12px;
            font-weight: 500;
        }}

        .engine-field small {{
            color: var(--text-muted);
            font-weight: 400;
        }}

        .engine-field input, .engine-field select, .engine-field textarea {{
            display: block;
            width: 100%;
            margin-top: 5px;
            padding: 8px 11px;
            color: var(--text-primary);
            background: var(--bg-input);
            border: 1px solid var(--border-medium);
            border-radius: 7px;
            font-family: inherit;
            font-size: 12px;
            outline: none;
            transition: border-color 0.15s;
        }}

        .engine-field input:focus, .engine-field select:focus, .engine-field textarea:focus {{
            border-color: var(--border-focus);
        }}

        .engine-field textarea {{
            min-height: 56px;
            resize: vertical;
        }}

        .engine-actions {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 14px;
        }}

        .engine-actions button {{
            padding: 7px 12px;
            border: 1px solid var(--border-medium);
            border-radius: 7px;
            color: var(--text-primary);
            background: var(--bg-surface-elevated);
            cursor: pointer;
            font-size: 11px;
            font-weight: 600;
            font-family: inherit;
            transition: all 0.15s;
        }}

        .engine-actions button:hover {{
            background: var(--bg-surface-hover);
            border-color: var(--border-strong);
        }}

        .engine-actions button.primary {{
            color: var(--btn-primary-text);
            border-color: var(--btn-primary-bg);
            background: var(--btn-primary-bg);
        }}

        .engine-actions button.primary:hover {{
            background: var(--btn-primary-hover);
            border-color: var(--btn-primary-hover);
        }}

        .output-label {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 14px 0 6px;
            color: var(--text-secondary);
            font-size: 11px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }}

        .char-counter {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            color: var(--text-muted);
        }}

        .char-warning {{
            color: var(--text-primary);
            font-weight: 700;
            text-decoration: underline;
        }}

        .output-box {{
            width: 100%;
            min-height: 70px;
            padding: 9px 11px;
            color: var(--text-primary);
            background: var(--bg-input);
            border: 1px solid var(--border-medium);
            border-radius: 7px;
            font: 12px/1.5 var(--font-sans, inherit);
            resize: vertical;
            outline: none;
            font-family: inherit;
        }}

        .output-box:focus {{
            border-color: var(--border-focus);
        }}

        .tabs-header {{
            display: flex;
            gap: 6px;
            margin-bottom: 8px;
        }}

        .char-limit-tab {{
            padding: 4px 9px;
            border-radius: 5px;
            font-size: 10px;
            font-weight: 600;
            border: 1px solid var(--border-medium);
            background: var(--bg-surface-elevated);
            color: var(--text-secondary);
            cursor: pointer;
        }}

        .char-limit-tab.active {{
            background: var(--text-primary);
            color: var(--text-inverted);
            border-color: var(--text-primary);
        }}

        /* Analytics Modal Cards */
        .analytics-card {{
            background: var(--bg-surface-elevated);
            border: 1px solid var(--border-subtle);
            border-radius: 8px;
            padding: 14px;
        }}

        .analytics-label {{
            font-size: 10px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--text-muted);
        }}

        .analytics-val {{
            font-size: 24px;
            font-weight: 800;
            font-family: 'JetBrains Mono', monospace;
            margin-top: 4px;
            color: var(--text-primary);
        }}

        .analytics-sub {{
            font-size: 11px;
            color: var(--text-secondary);
            margin-top: 2px;
        }}

        /* Toast notification */
        #toast {{
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: var(--toast-bg);
            color: var(--toast-text);
            padding: 9px 16px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 600;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
            border: 1px solid var(--border-medium);
            opacity: 0;
            transform: translateY(12px);
            transition: opacity 0.2s ease, transform 0.2s ease;
            pointer-events: none;
            z-index: 1001;
            font-family: inherit;
        }}

        #toast.show {{
            opacity: 1;
            transform: translateY(0);
        }}

        .footer {{
            margin-top: 32px;
            padding-top: 20px;
            border-top: 1px solid var(--border-subtle);
            text-align: center;
            font-size: 12px;
            color: var(--text-muted);
        }}

        #btn-more-actions-wrap {{
            display: none;
        }}

        /* Desktop Cards Mode (when manually enabled) */
        @media (min-width: 769px) {{
            .table-container.cards-mode {{
                background: transparent !important;
                border: none !important;
                box-shadow: none !important;
                overflow: visible !important;
                max-height: none !important;
                min-height: auto !important;
            }}

            .table-container.cards-mode table,
            .table-container.cards-mode tbody {{
                display: block !important;
                width: 100% !important;
            }}

            .table-container.cards-mode thead {{
                display: none !important;
            }}

            .table-container.cards-mode tbody {{
                display: grid !important;
                grid-template-columns: repeat(auto-fill, minmax(370px, 1fr)) !important;
                gap: 14px !important;
            }}

            .table-container.cards-mode tbody tr {{
                display: flex !important;
                flex-direction: column !important;
                gap: 10px !important;
                background: var(--bg-surface) !important;
                border: 1px solid var(--border-subtle) !important;
                border-radius: 12px !important;
                padding: 16px !important;
                box-shadow: var(--card-shadow) !important;
                position: relative !important;
                transition: border-color 0.15s, transform 0.15s !important;
            }}

            .table-container.cards-mode tbody tr:hover {{
                border-color: var(--border-medium) !important;
                transform: translateY(-1px) !important;
            }}

            .table-container.cards-mode td {{
                display: block !important;
                padding: 0 !important;
                border: none !important;
                width: 100% !important;
                min-width: 0 !important;
                max-width: none !important;
            }}

            .table-container.cards-mode .col-id {{
                position: absolute !important;
                top: 14px !important;
                right: 14px !important;
                width: auto !important;
                font-size: 11px !important;
                color: var(--text-muted) !important;
            }}

            .table-container.cards-mode .company-name-cell {{
                padding-right: 48px !important;
                border-bottom: 1px solid var(--border-subtle) !important;
                padding-bottom: 10px !important;
            }}

            .table-container.cards-mode .company-title {{
                font-size: 16px !important;
            }}

            .table-container.cards-mode .hook-cell {{
                background: var(--bg-surface-elevated) !important;
                border: 1px solid var(--border-subtle) !important;
                border-left: 3px solid var(--border-strong) !important;
                border-radius: 8px !important;
                padding: 10px 12px !important;
                font-size: 12px !important;
                margin: 2px 0 !important;
            }}

            .table-container.cards-mode .hook-text {{
                -webkit-line-clamp: 5 !important;
            }}

            .table-container.cards-mode .action-stack {{
                gap: 8px !important;
            }}

            .table-container.cards-mode .email-text {{
                max-width: 100% !important;
                background: var(--bg-input) !important;
                padding: 5px 8px !important;
                border: 1px solid var(--border-subtle) !important;
                border-radius: 6px !important;
                font-size: 12px !important;
            }}

            .table-container.cards-mode .status-select {{
                min-height: 38px !important;
                padding: 8px 12px !important;
                font-size: 13px !important;
                width: 100% !important;
                border-radius: 8px !important;
            }}

            .table-container.cards-mode td:last-child > div {{
                display: flex !important;
                gap: 8px !important;
                margin-top: 4px !important;
            }}

            .table-container.cards-mode .draft-btn {{
                flex: 2 !important;
                min-height: 40px !important;
                font-size: 13px !important;
                font-weight: 700 !important;
                border-radius: 8px !important;
            }}

            .table-container.cards-mode td:last-child .btn-copy {{
                flex: 1 !important;
                min-height: 40px !important;
                font-size: 13px !important;
                border-radius: 8px !important;
            }}
        }}

        /* Mobile Phone Layout (Screen width <= 768px) */
        @media (max-width: 768px) {{
            body {{
                padding: 12px;
                padding-top: max(12px, env(safe-area-inset-top));
                padding-bottom: max(24px, env(safe-area-inset-bottom));
                padding-left: max(12px, env(safe-area-inset-left));
                padding-right: max(12px, env(safe-area-inset-right));
            }}

            header {{
                flex-direction: column;
                align-items: stretch;
                gap: 12px;
                margin-bottom: 14px;
                padding-bottom: 14px;
            }}

            .header-title h1 {{
                font-size: 20px;
                line-height: 1.3;
            }}

            .header-title p {{
                font-size: 12px;
            }}

            .header-actions {{
                display: flex;
                flex-wrap: wrap;
                gap: 6px;
                width: 100%;
            }}

            /* Hide heavy buttons on mobile; they are accessible in More Actions */
            #btn-export-json,
            #btn-export-csv,
            #btn-import-trigger,
            #btn-reset-list {{
                display: none !important;
            }}

            #btn-more-actions-wrap {{
                display: inline-block !important;
            }}

            .metrics-grid {{
                grid-template-columns: repeat(2, 1fr);
                gap: 8px;
                margin-bottom: 14px;
            }}

            .metric-card {{
                padding: 10px 12px;
            }}

            .metric-val {{
                font-size: 22px;
            }}

            .metric-label {{
                font-size: 10px;
            }}

            .metric-sub {{
                display: none;
            }}

            .controls-card {{
                padding: 12px;
                gap: 10px;
                margin-bottom: 14px;
            }}

            .controls-top {{
                flex-direction: column;
                align-items: stretch;
                gap: 8px;
            }}

            .search-box {{
                flex: 1 1 100%;
                width: 100%;
            }}

            .selectors-group {{
                width: 100%;
                display: flex;
                flex-wrap: wrap;
                gap: 6px;
            }}

            .control-select {{
                flex: 1 1 calc(50% - 4px);
                min-width: 0;
                font-size: 12px;
                padding: 8px 10px;
            }}

            .view-toggle {{
                width: 100%;
            }}

            .view-toggle-btn {{
                flex: 1;
                justify-content: center;
                padding: 7px 6px;
            }}

            .controls-bottom {{
                flex-direction: column;
                align-items: stretch;
                gap: 8px;
            }}

            .count-showing {{
                font-size: 11px;
                text-align: right;
            }}

            /* Mobile cards view (default on mobile unless forced into table mode) */
            .table-container:not(.table-mode) {{
                background: transparent !important;
                border: none !important;
                box-shadow: none !important;
                overflow: visible !important;
                max-height: none !important;
                min-height: auto !important;
            }}

            .table-container:not(.table-mode) table,
            .table-container:not(.table-mode) tbody {{
                display: block !important;
                width: 100% !important;
            }}

            .table-container:not(.table-mode) thead {{
                display: none !important;
            }}

            .table-container:not(.table-mode) tbody {{
                display: grid !important;
                grid-template-columns: 1fr !important;
                gap: 12px !important;
            }}

            .table-container:not(.table-mode) tbody tr {{
                display: flex !important;
                flex-direction: column !important;
                gap: 10px !important;
                background: var(--bg-surface) !important;
                border: 1px solid var(--border-subtle) !important;
                border-radius: 12px !important;
                padding: 16px !important;
                box-shadow: var(--card-shadow) !important;
                position: relative !important;
            }}

            .table-container:not(.table-mode) td {{
                display: block !important;
                padding: 0 !important;
                border: none !important;
                width: 100% !important;
                min-width: 0 !important;
                max-width: none !important;
            }}

            .table-container:not(.table-mode) .col-id {{
                position: absolute !important;
                top: 14px !important;
                right: 14px !important;
                width: auto !important;
                font-size: 11px !important;
                color: var(--text-muted) !important;
            }}

            .table-container:not(.table-mode) .company-name-cell {{
                padding-right: 48px !important;
                border-bottom: 1px solid var(--border-subtle) !important;
                padding-bottom: 10px !important;
            }}

            .table-container:not(.table-mode) .company-title {{
                font-size: 16px !important;
            }}

            .table-container:not(.table-mode) .hook-cell {{
                background: var(--bg-surface-elevated) !important;
                border: 1px solid var(--border-subtle) !important;
                border-left: 3px solid var(--border-strong) !important;
                border-radius: 8px !important;
                padding: 10px 12px !important;
                font-size: 12px !important;
                margin: 2px 0 !important;
            }}

            .table-container:not(.table-mode) .hook-text {{
                -webkit-line-clamp: 6 !important;
            }}

            .table-container:not(.table-mode) .actions-cell {{
                padding-top: 4px !important;
            }}

            .table-container:not(.table-mode) .action-stack {{
                gap: 8px !important;
            }}

            .table-container:not(.table-mode) .email-text {{
                max-width: 100% !important;
                background: var(--bg-input) !important;
                padding: 6px 8px !important;
                border: 1px solid var(--border-subtle) !important;
                border-radius: 6px !important;
                font-size: 12px !important;
            }}

            .table-container:not(.table-mode) .btn-copy,
            .table-container:not(.table-mode) .btn-link {{
                min-height: 40px !important;
                padding: 8px 12px !important;
                font-size: 12px !important;
                flex: 1 1 auto !important;
            }}

            .table-container:not(.table-mode) .status-select {{
                min-height: 40px !important;
                padding: 8px 12px !important;
                font-size: 13px !important;
                width: 100% !important;
                border-radius: 8px !important;
            }}

            .table-container:not(.table-mode) td:last-child > div {{
                display: flex !important;
                gap: 8px !important;
                margin-top: 4px !important;
            }}

            .table-container:not(.table-mode) .draft-btn {{
                flex: 2 !important;
                min-height: 42px !important;
                font-size: 13px !important;
                font-weight: 700 !important;
                border-radius: 8px !important;
            }}

            .table-container:not(.table-mode) td:last-child .btn-copy {{
                flex: 1 !important;
                min-height: 42px !important;
                font-size: 13px !important;
                border-radius: 8px !important;
            }}

            /* Mobile Outreach Modal */
            .modal {{
                padding: 0 !important;
            }}

            .modal-card {{
                margin: 0 !important;
                max-width: 100% !important;
                min-height: 100vh !important;
                border-radius: 0 !important;
                border: none !important;
                padding: 16px !important;
                padding-bottom: max(32px, env(safe-area-inset-bottom)) !important;
            }}

            .modal-head {{
                position: sticky !important;
                top: 0 !important;
                background: var(--modal-bg) !important;
                z-index: 20 !important;
                padding-top: max(8px, env(safe-area-inset-top)) !important;
                margin-top: -16px !important;
                margin-left: -16px !important;
                margin-right: -16px !important;
                padding-left: 16px !important;
                padding-right: 16px !important;
            }}

            .engine-grid {{
                grid-template-columns: 1fr !important;
                gap: 14px !important;
            }}

            /* iOS auto-zoom prevention */
            .engine-field input,
            .engine-field select,
            .engine-field textarea,
            .output-box {{
                font-size: 16px !important;
            }}

            .engine-actions button {{
                min-height: 42px !important;
                font-size: 12px !important;
                flex: 1 !important;
            }}

            #toast {{
                left: 50% !important;
                right: auto !important;
                bottom: calc(16px + env(safe-area-inset-bottom)) !important;
                transform: translateX(-50%) translateY(12px) !important;
                max-width: calc(100vw - 32px) !important;
                width: max-content !important;
                text-align: center !important;
            }}

            #toast.show {{
                transform: translateX(-50%) translateY(0) !important;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="header-title">
                <h1>Target Startups: {total_count} Funded AI Startups (&lt;100 Employees)</h1>
                <p>Kumar Nalin · USAR 2027 · Pure Neutral Grayscale Outreach &amp; Conversion Desk</p>
            </div>
            <div class="header-actions">
                <button id="btn-add-company" class="action-btn action-btn-primary" title="Add a new startup to the outreach list">
                    <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
                    <span>+ Add Company</span>
                </button>
                <button id="btn-analytics" class="action-btn" title="Open conversion rate &amp; pipeline metrics">
                    <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>
                    <span>Analytics</span>
                </button>
                <a href="Kumar_Nalin_Resume_Final_Compact_v3.pdf" target="_blank" rel="noopener" class="action-btn" title="View or Download Kumar Nalin's Resume (PDF)">
                    <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                    <span>Resume</span>
                </a>
                <button id="btn-export-json" class="action-btn" title="Backup all outreach state to JSON">
                    <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                    <span>Export JSON</span>
                </button>
                <button id="btn-export-csv" class="action-btn" title="Export tracker spreadsheet to CSV">
                    <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                    <span>Export CSV</span>
                </button>
                <button id="btn-import-trigger" class="action-btn" title="Restore tracker state from backup file">
                    <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>
                    <span>Import Backup</span>
                </button>
                <input type="file" id="file-import-input" accept=".json,.csv" style="display: none;">
                <button id="btn-reset-list" class="action-btn" title="Reset directory to initial default list">
                    <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2.5 2v6h6M21.5 22v-6h-6"/><path d="M22 11.5A10 10 0 0 0 3.2 7.2M2 12.5a10 10 0 0 0 18.8 4.2"/></svg>
                    <span>Reset List</span>
                </button>
                <div class="more-actions-wrap" id="btn-more-actions-wrap">
                    <button id="btn-more-actions" class="action-btn" title="Data backup and management actions" aria-haspopup="true">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="1.5"></circle><circle cx="19" cy="12" r="1.5"></circle><circle cx="5" cy="12" r="1.5"></circle></svg>
                        <span>More</span>
                    </button>
                    <div class="more-actions-dropdown" id="more-actions-menu">
                        <button class="more-action-item" onclick="openStorageModal()">
                            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path></svg>
                            <span>Storage &amp; Backup</span>
                        </button>
                        <button class="more-action-item" onclick="document.getElementById('btn-export-json').click()">
                            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                            <span>Export JSON</span>
                        </button>
                        <button class="more-action-item" onclick="document.getElementById('btn-export-csv').click()">
                            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                            <span>Export CSV</span>
                        </button>
                        <button class="more-action-item" onclick="document.getElementById('btn-import-trigger').click()">
                            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>
                            <span>Import Backup</span>
                        </button>
                        <button class="more-action-item" onclick="document.getElementById('btn-reset-list').click()">
                            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.5 2v6h6M21.5 22v-6h-6"/><path d="M22 11.5A10 10 0 0 0 3.2 7.2M2 12.5a10 10 0 0 0 18.8 4.2"/></svg>
                            <span>Reset List</span>
                        </button>
                    </div>
                </div>
                <button id="theme-toggle" class="theme-toggle-btn" aria-label="Toggle theme">
                    <span class="theme-icon">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
                    </span>
                    <span class="theme-text">Light Mode</span>
                </button>
                <button id="btn-storage-modal" class="storage-status-btn" title="View Local Storage sync status &amp; backup options">
                    <span class="storage-dot" id="storage-status-dot"></span>
                    <span id="storage-status-text">Storage: Saved</span>
                </button>
                <div class="header-badge" id="pipeline-stat">0 / {total_count} In Pipeline</div>
            </div>
        </header>

        <!-- Metric Cards -->
        <div class="metrics-grid">
            <div class="metric-card">
                <div class="metric-label">Total Prospects</div>
                <div class="metric-val" id="metric-total">{total_count}</div>
                <div class="metric-sub">Verified &lt;100 team, Seed-B</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Tier A Leads</div>
                <div class="metric-val" id="metric-tier-a">{tier_a_count}</div>
                <div class="metric-sub">Deeply personalized outreach</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Tier B Leads</div>
                <div class="metric-val" id="metric-tier-b">{tier_b_count}</div>
                <div class="metric-sub">Semi-personalized + custom line</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">In Pipeline</div>
                <div class="metric-val" id="metric-pipeline">0</div>
                <div class="metric-sub">Connection or Email sent</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Follow-ups Due</div>
                <div class="metric-val" id="metric-followups">0</div>
                <div class="metric-sub">Due today or stale &gt;5d</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Replies &amp; Offers</div>
                <div class="metric-val" id="metric-replied">0</div>
                <div class="metric-sub">Active candidate pipeline</div>
            </div>
        </div>

        <!-- Controls Toolbar -->
        <div class="controls-card">
            <div class="controls-top">
                <div class="search-box">
                    <span class="search-icon">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                    </span>
                    <input type="text" id="search-input" placeholder="Search company, sector, contact name, location, score, or tech hook...">
                    <button class="search-clear" id="search-clear-btn" aria-label="Clear search">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                    </button>
                </div>
                <div class="selectors-group">
                    <select id="status-filter-select" class="control-select" aria-label="Filter by pipeline stage">
                        <option value="all">Stage: All records</option>
                        <option value="To Contact">Stage: To Contact</option>
                        <option value="Connection Sent">Stage: Connection Sent</option>
                        <option value="Accepted">Stage: Accepted</option>
                        <option value="DM Sent">Stage: DM Sent</option>
                        <option value="Email Sent">Stage: Email Sent</option>
                        <option value="Followed Up">Stage: Followed Up</option>
                        <option value="Replied">Stage: Replied</option>
                        <option value="Interview">Stage: Interview</option>
                        <option value="Offer">Stage: Offer</option>
                        <option value="Archived">Stage: Archived</option>
                    </select>
                    <select id="sort-select" class="control-select" aria-label="Sort companies">
                        <option value="score-desc">Sort: Total Score (25 to 0)</option>
                        <option value="score-asc">Sort: Total Score (0 to 25)</option>
                        <option value="id-asc">Sort: # ID (Ascending)</option>
                        <option value="id-desc">Sort: # ID (Descending)</option>
                        <option value="name-asc">Sort: Company Name (A-Z)</option>
                        <option value="name-desc">Sort: Company Name (Z-A)</option>
                        <option value="tier-asc">Sort: Tier (Tier A &rarr; C)</option>
                    </select>
                    <div class="view-toggle" id="view-toggle" role="group" aria-label="Layout view switcher">
                        <button class="view-toggle-btn active" data-view="auto" title="Auto view (cards on phone, table on desktop)">
                            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
                            <span>Auto</span>
                        </button>
                        <button class="view-toggle-btn" data-view="table" title="Force spreadsheet table view">
                            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
                            <span>Table</span>
                        </button>
                        <button class="view-toggle-btn" data-view="cards" title="Force cards view">
                            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="4" width="16" height="16" rx="2"></rect><line x1="4" y1="10" x2="20" y2="10"></line></svg>
                            <span>Cards</span>
                        </button>
                    </div>
                </div>
            </div>
            <div class="controls-bottom">
                <div class="filters-group">
                    <button class="filter-btn active" data-filter="all">All ({total_count})</button>
                    <button class="filter-btn" data-filter="tierA">Tier A ({tier_a_count})</button>
                    <button class="filter-btn" data-filter="tierB">Tier B ({tier_b_count})</button>
                    <button class="filter-btn" data-filter="tierC">Tier C ({tier_c_count})</button>
                    <button class="filter-btn" data-filter="today">Today (Follow-ups Due)</button>
                    <button class="filter-btn" data-filter="pipeline">In Pipeline</button>
                    <button class="filter-btn" data-filter="delhi">Delhi-NCR ({delhi_count})</button>
                    <button class="filter-btn" data-filter="remote">Remote ({remote_count})</button>
                </div>
                <div class="count-showing" id="count-showing">Showing {total_count} of {total_count} records</div>
            </div>
        </div>

        <!-- Table -->
        <div class="table-container" id="table-container">
            <table>
                <thead>
                    <tr>
                        <th style="width: 44px;">#</th>
                        <th style="width: 200px;">Company &amp; Tier</th>
                        <th style="width: 150px;">Sector / Domain</th>
                        <th style="width: 140px;">Location &amp; Size</th>
                        <th style="width: 170px;">Funding &amp; Warm Path</th>
                        <th style="width: 260px;">Suggested Hook</th>
                        <th style="width: 200px;">Contact &amp; Research</th>
                        <th style="width: 150px;">Pipeline Stage</th>
                        <th style="width: 140px;">Actions</th>
                    </tr>
                </thead>
                <tbody id="table-body">
                    <!-- Populated by JavaScript -->
                </tbody>
            </table>
        </div>

        <div class="footer">
            <p>Target Startups Directory · Kumar Nalin · USAR 2027 · Automated Link Audits &amp; Outreach Engine</p>
        </div>
    </div>

    <!-- Add / Edit Company Modal -->
    <div class="modal" id="company-form-modal" role="dialog" aria-modal="true" aria-labelledby="company-form-title">
        <div class="modal-card" style="max-width: 920px;">
            <div class="modal-head">
                <div>
                    <h2 id="company-form-title">Add New Startup / Company</h2>
                    <p style="color: var(--text-secondary); font-size: 12px; margin-top: 3px;">Customize fields, contact information, scoring criteria, and notes.</p>
                </div>
                <button class="close-btn" id="close-form-modal" aria-label="Close form">&times;</button>
            </div>
            <form id="company-form">
                <input type="hidden" id="edit-company-id">
                <div class="engine-grid">
                    <section class="engine-section">
                        <h3>Company &amp; Operations</h3>
                        <label class="engine-field">Company Name *
                            <input id="form-company-name" required placeholder="e.g. Acme AI">
                        </label>
                        <label class="engine-field">Website URL *
                            <input id="form-website" type="text" required placeholder="https://acme.ai">
                        </label>
                        <label class="engine-field">Sector / Domain
                            <input id="form-domain-sector" placeholder="e.g. AI Devtools &amp; Code Quality">
                        </label>
                        <label class="engine-field">Work Model &amp; Location
                            <input id="form-location" placeholder="e.g. Delhi-NCR (Noida) / Remote">
                        </label>
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                            <label class="engine-field">Team Headcount
                                <input id="form-employee-count" placeholder="e.g. 10-25">
                            </label>
                            <label class="engine-field">Funding &amp; Investors
                                <input id="form-funding" placeholder="e.g. Seed $2M (YC W24)">
                            </label>
                        </div>
                        <label class="engine-field">Careers Page URL
                            <input id="form-career-url" placeholder="https://acme.ai/careers">
                        </label>
                        <label class="engine-field">LinkedIn Profile / Company URL
                            <input id="form-linkedin-url" placeholder="https://linkedin.com/company/acme-ai">
                        </label>
                    </section>
                    
                    <section class="engine-section">
                        <h3>Contact, Scoring &amp; Outreach Hook</h3>
                        <div style="display: grid; grid-template-columns: 1.2fr 1fr; gap: 10px;">
                            <label class="engine-field">Contact Name
                                <input id="form-contact-name" placeholder="e.g. Anuruddh Mishra">
                            </label>
                            <label class="engine-field">Contact Role
                                <input id="form-contact-role" placeholder="e.g. Founder &amp; CEO">
                            </label>
                        </div>
                        <div style="display: grid; grid-template-columns: 1.2fr 1fr; gap: 10px;">
                            <label class="engine-field">Career / Direct Email
                                <input id="form-email" type="email" placeholder="founder@acme.ai">
                            </label>
                            <label class="engine-field">Warm Intro Path
                                <input id="form-warm-path" placeholder="e.g. YC Founder / Open Source PR">
                            </label>
                        </div>
                        <label class="engine-field">Personalized Hook / Pitch Angle
                            <textarea id="form-hook" rows="2" placeholder="Customized technical angle (e.g. Next.js dashboard, FastAPI gateway latency)"></textarea>
                        </label>
                        
                        <div style="background: var(--bg-surface-elevated); padding: 10px 12px; border-radius: 8px; border: 1px solid var(--border-subtle); margin-bottom: 12px;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                                <span style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; color: var(--text-primary);">5-Dimension Fit Score</span>
                                <span id="form-total-score-display" style="font-family: 'JetBrains Mono', monospace; font-size: 13px; font-weight: 800; color: var(--text-primary);">21/25</span>
                            </div>
                            <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 6px; font-size: 10px; color: var(--text-muted); text-align: center;">
                                <div>
                                    <span>Stack</span>
                                    <input type="number" id="score-stack" min="0" max="5" value="4" style="margin-top: 3px; text-align: center; padding: 4px;">
                                </div>
                                <div>
                                    <span>Signal</span>
                                    <input type="number" id="score-hiring" min="0" max="5" value="4" style="margin-top: 3px; text-align: center; padding: 4px;">
                                </div>
                                <div>
                                    <span>India</span>
                                    <input type="number" id="score-india" min="0" max="5" value="5" style="margin-top: 3px; text-align: center; padding: 4px;">
                                </div>
                                <div>
                                    <span>Warm</span>
                                    <input type="number" id="score-warm" min="0" max="5" value="4" style="margin-top: 3px; text-align: center; padding: 4px;">
                                </div>
                                <div>
                                    <span>Comp</span>
                                    <input type="number" id="score-comp" min="0" max="5" value="4" style="margin-top: 3px; text-align: center; padding: 4px;">
                                </div>
                            </div>
                        </div>

                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                            <label class="engine-field">Assigned Tier
                                <select id="form-tier">
                                    <option value="Tier A">Tier A (Deeply personalized)</option>
                                    <option value="Tier B">Tier B (Semi-personalized)</option>
                                    <option value="Tier C">Tier C (Reserve / Drip)</option>
                                </select>
                            </label>
                            <label class="engine-field">Pipeline Stage
                                <select id="form-status">
                                    <option value="To Contact">To Contact</option>
                                    <option value="Connection Sent">Connection Sent</option>
                                    <option value="Accepted">Accepted</option>
                                    <option value="DM Sent">DM Sent</option>
                                    <option value="Email Sent">Email Sent</option>
                                    <option value="Followed Up">Followed Up</option>
                                    <option value="Replied">Replied</option>
                                    <option value="Interview">Interview</option>
                                    <option value="Offer">Offer</option>
                                    <option value="Archived">Archived</option>
                                </select>
                            </label>
                        </div>
                    </section>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 18px; padding-top: 14px; border-top: 1px solid var(--border-subtle);">
                    <button type="button" id="btn-delete-company" class="action-btn btn-danger" style="display: none;">
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
                        <span>Delete Company</span>
                    </button>
                    <div style="display: flex; gap: 8px; margin-left: auto;">
                        <button type="button" id="btn-cancel-form" class="action-btn">Cancel</button>
                        <button type="submit" id="btn-save-company" class="action-btn action-btn-primary">Save Company</button>
                    </div>
                </div>
            </form>
        </div>
    </div>

    <!-- Outreach Modal Workbench -->
    <div class="modal" id="outreach-modal" role="dialog" aria-modal="true" aria-labelledby="modal-comp-name">
        <div class="modal-card">
            <div class="modal-head">
                <div>
                    <h2>
                        <span id="modal-comp-name">Company Name</span>
                        <span class="badge badge-tier-a" id="modal-comp-tier">Tier A</span>
                        <span class="badge badge-score" id="modal-comp-score">Score: 25/25</span>
                    </h2>
                    <div class="modal-meta">
                        <span id="modal-comp-sector">Sector</span> · <span id="modal-comp-location">Location</span> · 
                        <span id="modal-comp-contact">Founder</span> · <span id="modal-comp-email" style="font-family: 'JetBrains Mono', monospace;">email</span>
                        <span style="margin-left: 8px;">
                            <a id="modal-comp-website" href="#" target="_blank" rel="noopener" class="btn-link" style="padding: 2px 6px; font-size: 10px;">Website</a>
                            <a id="modal-comp-linkedin" href="#" target="_blank" rel="noopener" class="btn-link" style="padding: 2px 6px; font-size: 10px;">LinkedIn</a>
                            <button id="btn-edit-from-workbench" class="action-btn" style="padding: 2px 7px; font-size: 10px;">Edit Details</button>
                        </span>
                    </div>
                    <div class="score-breakdown-row" id="modal-score-breakdown">
                        <!-- Score breakdown injected here -->
                    </div>
                </div>
                <button class="close-btn" id="close-modal" aria-label="Close modal">&times;</button>
            </div>
            <div class="engine-grid">
                <section class="engine-section">
                    <h3>Research &amp; Personalization</h3>
                    <label class="engine-field">Target Feature or Signal
                        <input id="input-feature-signal" autocomplete="off" placeholder="e.g. AI Gateway, voice agents, memory API">
                    </label>
                    <label class="engine-field">Concrete Observation
                        <textarea id="input-observation" placeholder="One concrete technical observation from product/repo"></textarea>
                    </label>
                    <label class="engine-field">Proof Highlight (Select best fit for domain)
                        <select id="select-proof">
                            <option value="NimitAI 317s->117s Pipeline Win">NimitAI: cut LLM pipeline 317s->117s (63% latency reduction)</option>
                            <option value="Code Sage AST Engine">Code Sage: built AST-driven static analysis engine for code audits</option>
                            <option value="Notovo LangGraph Memory">Notovo: shipped agentic memory and structured note synthesis via LangGraph</option>
                            <option value="OceanRAG Retrieval">OceanRAG: sub-second vector search &amp; high-throughput retrieval</option>
                            <option value="TTS Audio Analysis">Prep War Room: speech analysis and low-latency audio workflows</option>
                        </select>
                    </label>
                    <label class="engine-field">Pipeline Stage
                        <select id="modal-status-select">
                            <option value="To Contact">To Contact</option>
                            <option value="Connection Sent">Connection Sent</option>
                            <option value="Accepted">Accepted</option>
                            <option value="DM Sent">DM Sent</option>
                            <option value="Email Sent">Email Sent</option>
                            <option value="Followed Up">Followed Up</option>
                            <option value="Replied">Replied</option>
                            <option value="Interview">Interview</option>
                            <option value="Offer">Offer</option>
                            <option value="Archived">Archived</option>
                        </select>
                    </label>
                    <div id="modal-date-info" style="font-size: 11px; font-family: 'JetBrains Mono', monospace; color: var(--text-muted); margin-bottom: 10px;"></div>
                    <label class="engine-field">Private Notes
                        <textarea id="modal-custom-notes" placeholder="Notes on replies, intro path, follow-up schedule..."></textarea>
                    </label>
                    <div class="engine-actions">
                        <button class="primary" id="btn-save-notes">Save Notes</button>
                    </div>
                </section>
                <section class="engine-section">
                    <h3>Generated Outreach Drafts</h3>
                    
                    <!-- LinkedIn Note -->
                    <div class="output-label">
                        <span>LinkedIn Connection Note</span>
                        <span id="linkedin-char-counter" class="char-counter">0/200 chars</span>
                    </div>
                    <div class="tabs-header">
                        <button class="char-limit-tab active" data-tier="free">Free Account (200 limit)</button>
                        <button class="char-limit-tab" data-tier="premium">Premium (300 limit)</button>
                    </div>
                    <textarea class="output-box" id="draft-linkedin-text" rows="3"></textarea>
                    <div class="engine-actions">
                        <button data-copy-target="draft-linkedin-text">Copy Note</button>
                        <button id="btn-mark-conn-sent">Mark Connection Sent</button>
                    </div>

                    <!-- First DM -->
                    <div class="output-label" style="margin-top: 14px;">
                        <span>First DM (After Acceptance &mdash; No Pitch)</span>
                    </div>
                    <textarea class="output-box" id="draft-dm-text" rows="3"></textarea>
                    <div class="engine-actions">
                        <button data-copy-target="draft-dm-text">Copy DM</button>
                        <button id="btn-mark-dm-sent">Mark DM Sent</button>
                    </div>

                    <!-- Cold Email -->
                    <div class="output-label" style="margin-top: 14px;">
                        <span>Cold Email (80&ndash;120 words)</span>
                        <span id="email-word-count" class="char-counter">0 words</span>
                    </div>
                    <input class="output-box" id="draft-email-subject" style="min-height: 36px; margin-bottom: 6px;">
                    <textarea class="output-box" id="draft-email-body" rows="6"></textarea>
                    <div class="engine-actions">
                        <button data-copy-target="draft-email-body">Copy Email</button>
                        <button id="btn-mark-email-sent">Mark Email Sent</button>
                    </div>

                    <!-- Follow Up -->
                    <div class="output-label" style="margin-top: 14px;">
                        <span>Day 5&ndash;7 Follow-up (2 sentences, fresh angle)</span>
                    </div>
                    <input class="output-box" id="draft-followup-subject" style="min-height: 36px; margin-bottom: 6px;">
                    <textarea class="output-box" id="draft-followup-body" rows="3"></textarea>
                    <div class="engine-actions">
                        <button data-copy-target="draft-followup-body">Copy Follow-up</button>
                        <button id="btn-mark-followup-sent">Mark Followed Up</button>
                    </div>
                </section>
            </div>
        </div>
    </div>

    <!-- Conversion Analytics Modal -->
    <div class="modal" id="analytics-modal" role="dialog" aria-modal="true" aria-labelledby="analytics-title">
        <div class="modal-card" style="max-width: 780px;">
            <div class="modal-head">
                <div>
                    <h2 id="analytics-title">Conversion Dashboard &amp; Analytics</h2>
                    <p style="color: var(--text-secondary); font-size: 12px; margin-top: 3px;">Acceptance rates, channel response rates, and pipeline conversion by tier</p>
                </div>
                <button class="close-btn" id="close-analytics-modal" aria-label="Close analytics">&times;</button>
            </div>
            <div id="analytics-modal-body">
                <!-- Rendered dynamically -->
            </div>
        </div>
    </div>

    <!-- Local Storage & Data Persistence Modal -->
    <div class="modal" id="storage-modal" role="dialog" aria-modal="true" aria-labelledby="storage-modal-title">
        <div class="modal-card" style="max-width: 680px;">
            <div class="modal-head">
                <div>
                    <h2 id="storage-modal-title">Local Storage &amp; Data Persistence</h2>
                    <p style="color: var(--text-secondary); font-size: 12px; margin-top: 3px;">Auto-saved in browser LocalStorage. Persists permanently across page refreshes and sessions.</p>
                </div>
                <button class="close-btn" id="close-storage-modal" aria-label="Close storage modal">&times;</button>
            </div>
            <div id="storage-modal-body">
                <!-- Rendered dynamically -->
            </div>
        </div>
    </div>

    <!-- Notification Toast -->
    <div id="toast">Copied to clipboard.</div>

    <script>
        const companies = {companies_json};
    </script>
    <script>
{engine_js}
    </script>
</body>
</html>"""

    viewer_path = os.path.join(os.path.dirname(__file__), "..", "company_directory_viewer.html")
    with open(viewer_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    index_path = os.path.join(os.path.dirname(__file__), "..", "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Successfully generated {viewer_path} and {index_path} with {total_count} companies!")

if __name__ == "__main__":
    generate_html_viewer()
