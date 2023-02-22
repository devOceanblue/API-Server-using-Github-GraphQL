import asyncio
import logging
from typing import List, Dict

import aiohttp
from gql import gql

import config

graphql_query = """
query {
  search(
    query: "name:airbnb",
    type:REPOSITORY, 
    first: 100
  ) {
    repos: edges {
      repo: node {
        ... on Repository {
          name
          description
          openIssues: issues(states:OPEN) {
            totalCount
          }
          fiveMostRecentIssues: issues(first:5, orderBy: {field: CREATED_AT, direction: DESC}){
              edges {
                  node {
                      title
                  }
              }
          }
        }
      }
    }
  }
}
"""

class RepositoryInfoService:
    async def get_repository_info(self, session: object, headers: Dict, name: str):
        async with session.post("https://api.github.com/graphql", json={'query': graphql_query}, headers=headers) as response:
            res = await response.json()
            return res
    async def get_repositories_info(self, repository_names: List[str]):
        headers = {"Authorization": f'Bearer {config.github_token}'}
        async with aiohttp.ClientSession() as session:
            results = await asyncio.gather(*[self.get_repository_info(session=session, headers=headers, name=name) for name in repository_names])
            return results

