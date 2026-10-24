import asyncio
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()

with open(r"C:\Users\user\Desktop\sharad-ai\shared\ey-ai-upskill-13\key-vault\ey-key\api.key") as f:
    openai_api_key = f.read().strip()

async def main():

    client = MultiServerMCPClient(
        {
            "cyber": {
                "transport": "stdio",
                "command": "python",
                "args": ["mcp_cyber_tools_server.py"],
            }
        }
    )

    tools = await client.get_tools()

    print("\nAvailable Tools\n----------------")
    for t in tools:
        print(t.name)

    llm = ChatOpenAI(
        model="gpt-4.1",
        api_key=openai_api_key,
        temperature=0,
    )

    agent = create_agent(
        model=llm,
        tools=tools,
    )

    # response = await agent.ainvoke(
    #     {
    #         "messages": [
    #             {
    #                 "role": "user",
    #                 "content": (
    #                     "Find recent Apache Struts CVEs and "
    #                     "also retrieve their EPSS score."
    #                 ),
    #             }
    #         ]
    #     }
    # )

    # print("\n===========================")
    # print(response["messages"][-1].content)

    
    # response = await agent.ainvoke(
    #     {
    #         "messages": [
    #             {
    #                 "role": "user",
    #                 "content": (
    #                     "Secure Apache HTTP Server and include recent CVEs, KEV entries, and ATT&CK techniques."
    #                 ),
    #             }
    #         ]
    #     }
    # )

    # print("\n===========================")
    # print(response["messages"][-1].content)


    
    # response = await agent.ainvoke(
    #     {
    #         "messages": [
    #             {
    #                 "role": "user",
    #                 "content": (
    #                     "Prioritize patching for CVE-2023-34362 using its EPSS score."
    #                 ),
    #             }
    #         ]
    #     }
    # )

    # print("\n===========================")
    # print(response["messages"][-1].content)

    
    # response = await agent.ainvoke(
    #     {
    #         "messages": [
    #             {
    #                 "role": "user",
    #                 "content": (
    #                     "Prepare a risk assessment for Microsoft Exchange Server using CIS guidance, CVEs, KEV, and EPSS."
    #                 ),
    #             }
    #         ]
    #     }
    # )

    # print("\n===========================")
    # print(response["messages"][-1].content)

    
    response = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        "Identify actively exploited vulnerabilities affecting VMware ESXi."
                    ),
                }
            ]
        }
    )

    print("\n===========================")
    print(response["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())