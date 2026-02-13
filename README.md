



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667G6UBTJT%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T124727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIFL52wqq5r2rAc6kEy%2FyRW6AndENifxBgl9L%2BPZ8YqYsAiEAjZzv6p4c3Q8I%2B28smGHr9vbV3G2WXToj3x3gNbmwa3gqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBnYBXJjwLtT7wkmiSrcAwGNMzEVlZip0CdIpQNQI7lD7mKAv0mX3xs7FlWVQID38I%2BvtkjFIpteeVb33LYkZYmQPaLn7Ne5imy74pKuZcLcH3buZkXLdTsvXjW8%2FnVKSMlT98eu9m02L8QyAT8oPOJwSA0j4PAgWDxwmHV6M06IPtZQADng1y5vM9%2BF3FxH%2B92s9RoCM8TqvP8VZE%2FIjVn6bbHB52BhnV%2F2ff0poypm4Vb6z%2Fw3xL1ZETGuZxeIDKyBbNNnPE8DqRYCW5tUITY2yP9AKzjhjydD7OrSY%2BLnzAkt86lJbMmB%2FWNw8kUfHyPPXZdl258nGxFdUsjYqvtLBiaDFo2ZeNh4NgaqnaK6m2rL3jMjWpdiwOoKq2ohM1724kf3KatAWDRFDe93WETUJGoWsPPNw3Ebgia0pizzB%2FoRZVgeS4Ck8H6TEXG0E%2BLftVCBlgAwjn7ANEDdxOGMNxcImfLzEnFZ7ZYocm70z73eUujMxTsSRHEsvEoksoKlzDfKHPRsmqEokdGa8NELpnDfmsVcDlWPzpkxpPlRqgRfvN6NOlkc2zS%2FVSyiLHJ49gxHfPoVRrTSRfIdVxiDzcBTEAYD3bq1JXZrT8C2i41Yh%2FaEZ8CUGHGyuH%2Bvl0gN5zW8PCjHxI3rMJKdvMwGOqUBxCYusuCoj90TzDJKL8O9ozPp45IaR3VRtje1hg%2BItWMGM4xg2q5h%2FLzZjqTLKisiD0TBY9xUhaJlxkUG3YvXqbh%2BfwO4ZHWmXbRF7UsQNDSw3dEYNxYqA3K5u33oAgtVe4lOSjopVQm2NSEGAuPzYbtPKJ0puvUdIDvtOaa3DP8%2BnVQq%2Fg1i9a2qse6vHLYoP4ZUpwXu%2B3dqGuYKM8CkI4TGNXv4&X-Amz-Signature=295ced13d9474dedb02556c2e4f6dbbceaac72a8329fcc6fb37e144ea64226b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667G6UBTJT%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T124727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIFL52wqq5r2rAc6kEy%2FyRW6AndENifxBgl9L%2BPZ8YqYsAiEAjZzv6p4c3Q8I%2B28smGHr9vbV3G2WXToj3x3gNbmwa3gqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBnYBXJjwLtT7wkmiSrcAwGNMzEVlZip0CdIpQNQI7lD7mKAv0mX3xs7FlWVQID38I%2BvtkjFIpteeVb33LYkZYmQPaLn7Ne5imy74pKuZcLcH3buZkXLdTsvXjW8%2FnVKSMlT98eu9m02L8QyAT8oPOJwSA0j4PAgWDxwmHV6M06IPtZQADng1y5vM9%2BF3FxH%2B92s9RoCM8TqvP8VZE%2FIjVn6bbHB52BhnV%2F2ff0poypm4Vb6z%2Fw3xL1ZETGuZxeIDKyBbNNnPE8DqRYCW5tUITY2yP9AKzjhjydD7OrSY%2BLnzAkt86lJbMmB%2FWNw8kUfHyPPXZdl258nGxFdUsjYqvtLBiaDFo2ZeNh4NgaqnaK6m2rL3jMjWpdiwOoKq2ohM1724kf3KatAWDRFDe93WETUJGoWsPPNw3Ebgia0pizzB%2FoRZVgeS4Ck8H6TEXG0E%2BLftVCBlgAwjn7ANEDdxOGMNxcImfLzEnFZ7ZYocm70z73eUujMxTsSRHEsvEoksoKlzDfKHPRsmqEokdGa8NELpnDfmsVcDlWPzpkxpPlRqgRfvN6NOlkc2zS%2FVSyiLHJ49gxHfPoVRrTSRfIdVxiDzcBTEAYD3bq1JXZrT8C2i41Yh%2FaEZ8CUGHGyuH%2Bvl0gN5zW8PCjHxI3rMJKdvMwGOqUBxCYusuCoj90TzDJKL8O9ozPp45IaR3VRtje1hg%2BItWMGM4xg2q5h%2FLzZjqTLKisiD0TBY9xUhaJlxkUG3YvXqbh%2BfwO4ZHWmXbRF7UsQNDSw3dEYNxYqA3K5u33oAgtVe4lOSjopVQm2NSEGAuPzYbtPKJ0puvUdIDvtOaa3DP8%2BnVQq%2Fg1i9a2qse6vHLYoP4ZUpwXu%2B3dqGuYKM8CkI4TGNXv4&X-Amz-Signature=3be886faa8121098ab640f253712b1547bcb7c6f8f362ed96854314dc71a4f6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







