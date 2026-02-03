# --- 1. Area Code Tests (Must be 3 digits) ---
area_cases = ["654", "fff", "8765"]
for code in area_cases:
    if len(code) == 3 and code.isdigit():
        print(f"Area Code {code}: Accepted")
    else:
        print(f"Area Code {code}: Rejected")

# --- 2. Prefix Tests (No 0 or 1 at start) ---
prefix_cases = ["987", "077", "12d"]
for pre in prefix_cases:
    if len(pre) == 3 and pre.isdigit() and pre[0] not in ['0', '1']:
        print(f"Prefix {pre}: Accepted")
    else:
        print(f"Prefix {pre}: Rejected")

# --- 3. Password Tests (6 Alphanumeric) ---
pass_cases = ["458769", "1@hy45", "sse33"]
for pwd in pass_cases:
    if len(pwd) == 6 and pwd.isalnum():
        print(f"Password {pwd}: Accepted")
    else:
        print(f"Password {pwd}: Rejected")

# --- 4. Deposit Tests (Max 50,000) ---
deposit_cases = [20500, 81000, 500]
for amt in deposit_cases:
    if 1000 <= amt <= 50000:
        print(f"Deposit {amt}: Accepted")
    else:
        print(f"Deposit {amt}: Rejected")
