



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD756CXB%2F20261002%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261002T181038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG9X5t3UwNWTkHmx4BO3%2BigeEMVBFpOEdoMQLZkiAVkGAiBwOl3ISlt5Vdj%2FXoX2O5%2FkQVNNkV11gL4EqcsFkVdc2SqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDz0mCEeLfGwsOjd3KtwDBcKCZekOqLWsD81eAeKskVyzu14piyLjZgFG9cuqULbJkhUMAmCBhN1Pqp7TNY0JF%2FoaKux8y7FDhLWBcwX9mQ0eele99b2ZGEq7a3%2FXLK6fIqg5vaZWmIVLFx98YsRLlIv%2BTCE4Eya2V6Ou8Bzqf2qd93civ67zlwD09tgGaTOmj0KYnX1M4Vn93AD6LI%2BNX3%2Fm7WBKaxdYAOIrQjuN%2F8CHSqZwOKrGMCCBN0%2B0bUsVP4OnwoK9ff8YyjNypvOoSPd3gLDRfAZDlWu5NowRwciBzscdKcNGzKzmftY6pnB%2Fn52zC9qvbzFq4jAmRr8X%2BcRTfXY8q4cIwY0iZ4BnRNJouvKVmG%2BQqEA1HReje3wGutZ5dkG2E6EVCwCUiZ5al5Bb0DC%2FESk4lDKnD3GYv6UEc0Ej5jRhqzQQhkHIC1xBT1nHJsgy5VXFGWBWTizuki7mbPotUqFnPTmALum5iLl8WMu7RV9ZW7A6t5PYXEwkuu2rH6BwVHuVXSycgsujGzle6cjM8fHI21QnNJGipAl3%2FQRBaM8k0EqvaVLjwyQ5VOjgGwX1HqoJB%2BuH0JqvuvadjzjdSnj4DcDvLU8waQ9BlfmXCVxUbv3h6jEdLeSUx5MpgPq9kjWP1kcw87X%2F1QY6pgHoUhSab8JMOhlfdJQVj6jbxD3gZxRS9O3xaazrPapOMEkiyWmTZYkZdLIWUQAEQ8aXtObHuROmW8DUAcFM%2FlvRwyxXvayih637YTU1sWcJMZcZnMkAaKtSbigeOoxTP8r31XADryXewNjHp%2FrfFBf9YtpRyuG2RVxkqu9b8SN5HVpAZ3CRbYji1f5Fig9A5qEFeBzRruGJUw3txox3yLyI7RM85DSP&X-Amz-Signature=809cd3daa2477b40e76c274ecc221b25206d094a9904a48abc44ca8263875a44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD756CXB%2F20261002%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261002T181038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG9X5t3UwNWTkHmx4BO3%2BigeEMVBFpOEdoMQLZkiAVkGAiBwOl3ISlt5Vdj%2FXoX2O5%2FkQVNNkV11gL4EqcsFkVdc2SqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDz0mCEeLfGwsOjd3KtwDBcKCZekOqLWsD81eAeKskVyzu14piyLjZgFG9cuqULbJkhUMAmCBhN1Pqp7TNY0JF%2FoaKux8y7FDhLWBcwX9mQ0eele99b2ZGEq7a3%2FXLK6fIqg5vaZWmIVLFx98YsRLlIv%2BTCE4Eya2V6Ou8Bzqf2qd93civ67zlwD09tgGaTOmj0KYnX1M4Vn93AD6LI%2BNX3%2Fm7WBKaxdYAOIrQjuN%2F8CHSqZwOKrGMCCBN0%2B0bUsVP4OnwoK9ff8YyjNypvOoSPd3gLDRfAZDlWu5NowRwciBzscdKcNGzKzmftY6pnB%2Fn52zC9qvbzFq4jAmRr8X%2BcRTfXY8q4cIwY0iZ4BnRNJouvKVmG%2BQqEA1HReje3wGutZ5dkG2E6EVCwCUiZ5al5Bb0DC%2FESk4lDKnD3GYv6UEc0Ej5jRhqzQQhkHIC1xBT1nHJsgy5VXFGWBWTizuki7mbPotUqFnPTmALum5iLl8WMu7RV9ZW7A6t5PYXEwkuu2rH6BwVHuVXSycgsujGzle6cjM8fHI21QnNJGipAl3%2FQRBaM8k0EqvaVLjwyQ5VOjgGwX1HqoJB%2BuH0JqvuvadjzjdSnj4DcDvLU8waQ9BlfmXCVxUbv3h6jEdLeSUx5MpgPq9kjWP1kcw87X%2F1QY6pgHoUhSab8JMOhlfdJQVj6jbxD3gZxRS9O3xaazrPapOMEkiyWmTZYkZdLIWUQAEQ8aXtObHuROmW8DUAcFM%2FlvRwyxXvayih637YTU1sWcJMZcZnMkAaKtSbigeOoxTP8r31XADryXewNjHp%2FrfFBf9YtpRyuG2RVxkqu9b8SN5HVpAZ3CRbYji1f5Fig9A5qEFeBzRruGJUw3txox3yLyI7RM85DSP&X-Amz-Signature=0afc6a201a5d0c20e9680627de82f5a2c0a2ee185e5d49bcfa6696a4f04ebec5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







