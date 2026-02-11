import time
import sys

def type_writer(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def loading_bar(task):
    type_writer(task)
    for i in range(30):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(0.05)
    print(" ✔\n")

# Presentation Start
type_writer("🎤 Welcome everyone to my 5-minute ETL presentation!", 0.04)
time.sleep(0.5)

type_writer("Today, we will see how data is collected from the internet...", 0.04)
time.sleep(0.5)

loading_bar("🔍 Initializing Data Collector")

type_writer("📊 Detecting data sources...", 0.04)

sources = [
    "🌐 APIs (Social Media, Payments)",
    "🕸 Web Scraping (Websites, Prices)",
    "🗄 Databases",
    "📁 CSV & Excel Files",
    "📡 IoT Sensors & Logs"
]

for s in sources:
    type_writer("   " + s, 0.03)
    time.sleep(0.3)

loading_bar("🚀 ETL System Ready")
print('fun fact before we start : Hacking tools tend to evolve faster than cybersecurity measures because attackers can rapidly share exploits and automate attacks, while defenders must carefully design, test, and deploy protective systems')

type_writer("Let’s start collecting real data now!\n", 0.04)
