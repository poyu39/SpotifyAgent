import asyncio
from agent import SpotifyAgent


def main():
    print("🎵 Spotify Agent 啟動，輸入指令來控制音樂 (輸入 exit 結束)：\n")
    
    agent_wrapper = SpotifyAgent(
        base_url="http://localhost:11434/v1",
        api_key="ollama",
        model="qwen2.5"
    )
    
    agent_wrapper.create_agent()
    
    while True:
        user_input = input("user：")
        if user_input.lower() in ['exit', 'quit']:
            break
        
        response = asyncio.run(agent_wrapper.run_workflow(user_input))
        
        print(f'agent：{response.final_output}')


if __name__ == '__main__':
    main()
