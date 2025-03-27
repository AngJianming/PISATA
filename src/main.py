import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.agents.trading_agent import main as run_agent

if __name__ == "__main__":
    print("🚀 Starting PISATA AI Trading System...")
    print("💫 Remember: Trade safe and smart!")
    
    try:
        run_agent()
    except KeyboardInterrupt:
        print("\n👋 PISATA AI Trading System shutting down gracefully...")
    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")
        print("🔧 PISATA suggests checking the logs and trying again!")
