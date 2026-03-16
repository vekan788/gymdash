import re

# Read current index.html
with open('index.html', 'r') as f:
    content = f.read()

# Mock workout data: Bench 100kg 5x5
new_log = """
                <!-- New Mock Workout -->
                <div class=\"flex items-center justify-between p-3 rounded-xl bg-white/5 hover:bg-white/10 transition-colors cursor-pointer\">
                    <div class=\"flex items-center gap-4\">
                        <div class=\"h-10 w-10 rounded-full bg-green-500/20 text-green-400 flex items-center justify-center\">
                            <svg xmlns=\"http://www.w3.org/2000/svg\" class=\"h-5 w-5\" viewBox=\"0 0 20 20\" fill=\"currentColor\"><path fill-rule=\"evenodd\" d=\"M12 7a1 1 0 110-2h5a1 1 0 011 1v5a1 1 0 11-2 0V8.414l-4.293 4.293a1 1 0 01-1.414 0L8 10.414l-4.293 4.293a1 1 0 01-1.414-1.414l5-5a1 1 0 011.414 0L11 10.586 14.586 7H12z\" clip-rule=\"evenodd\" /></svg>
                        </div>
                        <div>
                            <p class=\"font-bold text-sm\">Bench Press (Mock)</p>
                            <p class=\"text-xs text-gray-500\">Today, 5:00 PM</p>
                        </div>
                    </div>
                    <p class=\"font-bold text-green-400\">100kg 5x5</p>
                </div>
"""

# Insert into the \"Recent Trades\" / Activity div
# Finding the div container for Recent Trades/Activity
pattern = r'(<!-- Recent Logs / PRs -->.*?<div class=\"space-y-4\">)'
content = re.sub(pattern, r'\1' + new_log, content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)
