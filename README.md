



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MM6FW7Y%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T075448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDE73RLz7kZgPuCFQJfFFyvybyc86NhCd4ZE%2B4vcrZYVAIhAI5BiHjrx%2FFt2h6CbXD3Xn1Z7LS910sqH2iFMMIjzh7mKv8DCHQQABoMNjM3NDIzMTgzODA1Igw1jgEEY%2ByGn9pBToYq3AOrY6IztAeHF2qI8eFegXk4Xnr2K7qbYbh6cIutbEDxEdYsqiiu%2BbVySJZ7de%2FxT05bCYjGJBPUxRLu0tipZlAOdmZIZiZ%2FNydU2jWSHMgMikk0GBq1nr8HnyhdwYoZns9UidMBrtza%2FvB9mdtimLGIumU2nXPPnTJrzi0Zvw8HHVR5LjiaOs%2FwUOEwY22ti%2BZOWomvQ%2BBlBTCXPAbCxeb4hwNbVRDP7opTE45quklqIuGSirasLA4gtQdCLrPwAbNx2Ac69VMGkrUza%2FD9bScGajIEeSGB5HbblRNwykSxamsijgr53xAGEYZAzSAijKCl%2FJZrXve3QqxKP%2Bj%2FKdJ1AXCAM7F2hfj8uzwzzGb4IlsyOi%2Fzg7%2BCH5dfVrKISSqeQ6RNOYHUAQOu5NUm1u2rAls%2FccpOTCMTRR8xbhE5jbiSBE3Yq0Kbcj8aU%2Fx6l2OmaeGd%2BS8lHx7MajKVK7NPALtPRoQjXLrcHEoPJsXpVf8Fvds5f7JvgCNxPICBWjpZbL2BhOnMDARJHLS0hQemtBxiDBf4ewyd6HMMs66n3mS%2BB%2BbFskayJQ3tUVTfBLYtxNEHC1V%2BV1qXgjb73oRUPMtg92S9P1q%2BDSQExHzPVygZFnxG9XH3HL95DjDfrKvPBjqkASfMh1fie%2BZGAW%2F4YpX%2FlaiSR7t6Y6NI9pXoyM4FwbynBA8ziJbIggr0nPkCdhj%2B3Y%2BqBgLmndqV6m5xPv0Ifg12XZfrro%2F%2F1WpcpfB1JKz3dpob2XqNd6Yw%2BA2e8a8p6SNLWJIMuXFamlXOupMpW%2Bpfq4WXBYc%2FNh4EA0kNqqhkpCB3Ky9N9OKvpsKYTn0JOyahUqWMYLd32mceTl7RolFOhxxO&X-Amz-Signature=c79db646f63dc25edf57be23eaaa1abc0f91ff168bb8a5475e5943a08bf08fbb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MM6FW7Y%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T075448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDE73RLz7kZgPuCFQJfFFyvybyc86NhCd4ZE%2B4vcrZYVAIhAI5BiHjrx%2FFt2h6CbXD3Xn1Z7LS910sqH2iFMMIjzh7mKv8DCHQQABoMNjM3NDIzMTgzODA1Igw1jgEEY%2ByGn9pBToYq3AOrY6IztAeHF2qI8eFegXk4Xnr2K7qbYbh6cIutbEDxEdYsqiiu%2BbVySJZ7de%2FxT05bCYjGJBPUxRLu0tipZlAOdmZIZiZ%2FNydU2jWSHMgMikk0GBq1nr8HnyhdwYoZns9UidMBrtza%2FvB9mdtimLGIumU2nXPPnTJrzi0Zvw8HHVR5LjiaOs%2FwUOEwY22ti%2BZOWomvQ%2BBlBTCXPAbCxeb4hwNbVRDP7opTE45quklqIuGSirasLA4gtQdCLrPwAbNx2Ac69VMGkrUza%2FD9bScGajIEeSGB5HbblRNwykSxamsijgr53xAGEYZAzSAijKCl%2FJZrXve3QqxKP%2Bj%2FKdJ1AXCAM7F2hfj8uzwzzGb4IlsyOi%2Fzg7%2BCH5dfVrKISSqeQ6RNOYHUAQOu5NUm1u2rAls%2FccpOTCMTRR8xbhE5jbiSBE3Yq0Kbcj8aU%2Fx6l2OmaeGd%2BS8lHx7MajKVK7NPALtPRoQjXLrcHEoPJsXpVf8Fvds5f7JvgCNxPICBWjpZbL2BhOnMDARJHLS0hQemtBxiDBf4ewyd6HMMs66n3mS%2BB%2BbFskayJQ3tUVTfBLYtxNEHC1V%2BV1qXgjb73oRUPMtg92S9P1q%2BDSQExHzPVygZFnxG9XH3HL95DjDfrKvPBjqkASfMh1fie%2BZGAW%2F4YpX%2FlaiSR7t6Y6NI9pXoyM4FwbynBA8ziJbIggr0nPkCdhj%2B3Y%2BqBgLmndqV6m5xPv0Ifg12XZfrro%2F%2F1WpcpfB1JKz3dpob2XqNd6Yw%2BA2e8a8p6SNLWJIMuXFamlXOupMpW%2Bpfq4WXBYc%2FNh4EA0kNqqhkpCB3Ky9N9OKvpsKYTn0JOyahUqWMYLd32mceTl7RolFOhxxO&X-Amz-Signature=bd7fb8ee5c7912c69e8341750a74662193e3fc630c494afc523b200cddb57198&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







