



ODATA —> Open Data Protocol 

                  (ISO International Organization for Standardization/

               IEC International Electrotechnical Commission approved)

    

    OASIS (Organization for the Advancement of Structured Information Standards) standard that defines a set of best practices for building and consuming RESTful APIs

     

## What is API?

    API (Application Programming Interface) is a set of rules, protocols, and tools that allows different software applications to communicate with each other.

## Four different ways API can work

    1. SOAP APIs:- XML, Used in past
    2. RPC APIs:- Remote Procedure Calls
    3. WebSocket APIs:- Used JSON objects, two way communication
    4. REST API: - Most Popular
    

# REST Principles/ 
architectural constraints

    

```mermaid

flowchart LR
  A[REST]
  A --> B[Uniform Interface]
  A --> C[Statelessness]
  A --> D[Client-Server]
  A --> E[Cacheabilit]
  A --> F[Layered System]
  A --> G[Code on Demand]
  
  style A fill:#64bef9, stroke:#000, stroke-width:2px,color:#000
  style B fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style A fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style C fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style D fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style E fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style F fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style G fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000

```

## Uniform Interface

    It indicates Server transfers information in a standard format.

    5. The formatted resource is called a Representation in REST.
    6. Request should identify recourses by using URI
    7. Clients have enough information in the resource representation to modify, delete the resource. The server meets this condition by sending metadata that describes the resource further. 
    8. Client receive information about how to process the representation further. The server achieves this by sending self descriptive messages that contain metadata about how the client can best use them.
    9. For other related resourses server sends hyperlink in the represenation. So client can dynamically discover more resources.
    

## Statelessness

    

    10. Communication method in which the server completes every client request independently of all previous request.
## Layered System

    

    The client can connect to other authorized intermediaries between client and server.

## Catchability

    It stores some responses on the client or an intermediary to improve server response time.

## Code on Demand

    Server can temporarily extend or customize client functionality by transferring softare programming code to client

    Example:

    When you fill registration form on any websites, your browser heighlights mistake. Such as incorrect phone number. It can do this by the code sent by server. 

    

    

    



```mermaid
graph LR
  A[ODATA]--as --> B[Web SQL]
  style A fill:#0287de
  style B fill:#0287de
```





## Remote API vs Web API

Remote API: designed to interact with communication network. By remote, we mean that resources being manipulated by the API are somewhere outside computer making the request.



Web API: Communication Network(WWW)

ALL Web services are APIs, but not all APIs are web services.

## What does the RESTful API Client Request contain?

1. Unique recourse identifier:- URI ⇒ (URL- Location + URN-Name)
1. HTTP Method: GET, POST, DELETE, PUT, PATCH
1. HTTP Headers: Extra information


## What does the RESTful API server response contain?



- Status  line 
  1XX :- Informational → Processing 102

  2XX :- Success →Ok 200, Ok Created 201

  3XX :- Redirection → moved to new URL 301

  4XX :- Client Side Error → Bad request 400

  5XX:- Server Side Error → Not implemented 501



- Message body
  Contains recourse representation

-  Header


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHMPJVYH%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T012432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFvHNtSI701Z30NudQFT6ALoNt0Zj5%2FFAfVlsSnKkxjnAiEA16GB0r317XpzLP52eSRIh03lAstgvZUXdDBWNT0B4nUq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDNCG65Ed%2F3nMS2OcRircA9rKKCFTwIhhCasqu4SXBF5P3MGmx5Mv%2F%2FrhTiLYL%2BmaD7gp1rsxLhyOUIWoXMjcLGckgxcDA5xL6KRnD23WnoNeLoyoTNTTC%2BDfiR5LxYRyIxN6Gi%2FrFKYQOwlhqLFjSkG%2Fo2Xm%2FjlYJL5Gt5OG%2FluaHKvwB%2BnsBk9bTmRjrzQ3Bx7VG7%2BwVwFATvycDdNHi%2Bk8tWKewwZJgfRc0B4eJQo27K0ly1GRRwR82bIggUG6bQYNg51MT%2B7txm50FJs4otF9ZyBk%2F2J0rBzW85Vf4mTG5XYxvL2we2dO2AvsyB%2BNrl0NzlbIggE983VOVqE%2FkpCkcxPA0YoO%2FzoSAXmioUd%2Byv97E1%2FoPOhRKgb0ii9nrGccBWw2pnuxLTgnw%2BXLDru6FryaFTv6MJT9Kz1d%2B2ylTSj2Qn0L7VHA1bwnllZU4TvxvmzSdRiq9wcR843%2FNahdhPudSuDWj8KEqjW1ZnoOzmXD4AelT1AaXxe74yfvN4kuM88QTuIr3CPkWzJev%2Ff0dqCsrjNZGscrITTrj2IfVH%2BeUutW%2F0iRhVP1oOaVBH24xVyW2%2FYvpk5flGWyt06AsU9I1gsbSnIcuBDR7Ck8a7gaLpgMSo0ZBXanQUV%2FMkKBRmbSBApOi2PnMO%2F%2B38sGOqUBF%2FwzfAbRsx8bpVygmSVfylu92S5qOBbw0hfJX93u10fOk8byKP1M2ggG5rjCMx5FLxTYphj72qR5SHt6qOQIvGHAnGdscL6iU5U2XnhmY2lTIxBqeTXyWEMqAvBocrFBh3ynaX5VjMao94rIu5CUipWVgPv1CfyK6A74xE%2BpaaW6R1ldGAFbvLDBjXptWftrRe7jGHr1sm6tNi%2FyTz%2BON99vmXjy&X-Amz-Signature=872c649db7d33f3a85f1bea7144d39474fd0892eef11b8c86b34eed63060319f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHMPJVYH%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T012432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFvHNtSI701Z30NudQFT6ALoNt0Zj5%2FFAfVlsSnKkxjnAiEA16GB0r317XpzLP52eSRIh03lAstgvZUXdDBWNT0B4nUq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDNCG65Ed%2F3nMS2OcRircA9rKKCFTwIhhCasqu4SXBF5P3MGmx5Mv%2F%2FrhTiLYL%2BmaD7gp1rsxLhyOUIWoXMjcLGckgxcDA5xL6KRnD23WnoNeLoyoTNTTC%2BDfiR5LxYRyIxN6Gi%2FrFKYQOwlhqLFjSkG%2Fo2Xm%2FjlYJL5Gt5OG%2FluaHKvwB%2BnsBk9bTmRjrzQ3Bx7VG7%2BwVwFATvycDdNHi%2Bk8tWKewwZJgfRc0B4eJQo27K0ly1GRRwR82bIggUG6bQYNg51MT%2B7txm50FJs4otF9ZyBk%2F2J0rBzW85Vf4mTG5XYxvL2we2dO2AvsyB%2BNrl0NzlbIggE983VOVqE%2FkpCkcxPA0YoO%2FzoSAXmioUd%2Byv97E1%2FoPOhRKgb0ii9nrGccBWw2pnuxLTgnw%2BXLDru6FryaFTv6MJT9Kz1d%2B2ylTSj2Qn0L7VHA1bwnllZU4TvxvmzSdRiq9wcR843%2FNahdhPudSuDWj8KEqjW1ZnoOzmXD4AelT1AaXxe74yfvN4kuM88QTuIr3CPkWzJev%2Ff0dqCsrjNZGscrITTrj2IfVH%2BeUutW%2F0iRhVP1oOaVBH24xVyW2%2FYvpk5flGWyt06AsU9I1gsbSnIcuBDR7Ck8a7gaLpgMSo0ZBXanQUV%2FMkKBRmbSBApOi2PnMO%2F%2B38sGOqUBF%2FwzfAbRsx8bpVygmSVfylu92S5qOBbw0hfJX93u10fOk8byKP1M2ggG5rjCMx5FLxTYphj72qR5SHt6qOQIvGHAnGdscL6iU5U2XnhmY2lTIxBqeTXyWEMqAvBocrFBh3ynaX5VjMao94rIu5CUipWVgPv1CfyK6A74xE%2BpaaW6R1ldGAFbvLDBjXptWftrRe7jGHr1sm6tNi%2FyTz%2BON99vmXjy&X-Amz-Signature=c2e22886e209f59fe2991d97dae0da93344a6ff9644a93c09a48d53e58a3a85f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





For HTTP PORT is 80



What is ODATA?

  ODATA is a Web protocol based om REST, for querying and updating Data.

Applying and building on Web technologies such as

  1. HTTP
  2. Atom publishing Protocol
  3. RSS ( Really Simple Syndication) 


Provide access information from Variety of applications.



## 

```mermaid
graph LR
  A[ODATA]
  A --> B[Format]
  A --> C[Protocol]
```

Format:- How data is described and how it is serialized.

Protocol:- How that Data is manipulated.



Origin of ODATA format





Final Test







