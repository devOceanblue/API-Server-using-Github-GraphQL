import asyncio
import logging
from typing import List, Dict

import aiohttp
from fastapi import HTTPException

import config



class RepositoryInfoService:
    def _parse_data(self, results) -> List[Dict]:
        """parse result of github GraphQL API.

        Parameters:
        name (List): result of github GraphQL API

        Returns:
        List[Dict]: parsed result.
       """

        return [r['data']['search'] for r in results]

    def _get_graphql_query_with_name(self, name: str) -> str:
        """insert parameter(name) into graphql query.

        Parameters:
        name (str): name of github repository to search

        Returns:
        str: complete graphql query with inserted arguments.
       """
        graphql_query = f"""
        query {{
          search(
            query: "name:airbnb",
            type:REPOSITORY, 
            first: 100
          ) {{
            repos: edges {{
              repo: node {{
                ... on Repository {{
                  name
                  description
                  openIssues: issues(states:OPEN) {{
                    totalCount
                  }}
                  fiveMostRecentIssues: issues(first:5, orderBy: {{field: CREATED_AT, direction: DESC}}){{
                      edges {{
                          node {{
                              title
                          }}
                      }}
                  }}
                }}
              }}
            }}
          }}
        }}
        """
        return graphql_query


    async def get_repository_info(self, session: object, headers: Dict, name: str):
        query = self._get_graphql_query_with_name(name)
        async with session.post("https://api.github.com/graphql", json={'query': query}, headers=headers) as response:
            res = await response.json()
            if res.get('errors'):
                logging.error(f"Invalid Request, Requested GraphQL query:{query}")
                raise HTTPException(status_code=400, detail="Invalid Request")
            return res
    async def get_repositories_info(self, repository_names: List[str]):
        headers = {"Authorization": f'Bearer {config.github_token}'}
        try:
            async with aiohttp.ClientSession() as session:
                results = await asyncio.gather(*[self.get_repository_info(session=session, headers=headers, name=name) for name in repository_names])
                return self._parse_data(results)
        except Exception as e:
            logging.error(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")

