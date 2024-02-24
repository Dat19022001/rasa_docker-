# import aiohttp
# import asyncio

# async def make_request(session, url, headers, payload):
#     async with session.post(url, headers=headers, data=payload) as response:
#         return await response.json()

# async def main():
#     api_url = "http://localhost:8000/api/user"
#     headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
#     payload = {"idChat": "1234"}

#     async with aiohttp.ClientSession() as session:
#         responses = await asyncio.gather(
#             make_request(session, api_url, headers, payload),
#             # Add more make_request calls if needed
#         )
#         print(responses)
#         user_name = responses[0]['User']
#         print(user_name)

#     # Process responses as needed

# asyncio.run(main())


