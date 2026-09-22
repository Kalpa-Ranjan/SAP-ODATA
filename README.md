



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SKTNCSU%2F20260922%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260922T002045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDSRMNLR%2BDZSM%2FZt%2Bnle04H4G4eLZd%2BZd81wJdznoeEvAiA6uHmHspMDbOtvjWhW2UnDS6sRU8ah9%2FfI3qht9aALGSqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5W72fV4A6yzgRuC6KtwD5sgMGOH86DDoVkzllhb%2BWeDbEcImSwokYJ7bp3%2FwzsiUBH4UMQywkviwGIGW%2FScmHcHu1jTYg%2BrZROBicZImY4QXLh%2Bs33fPg4DOo1fev3KliVIWER0iQgvBCmIrbhIHTcQc0dCiXYHNBrA1hhVWE1OYqiN6h1zafW8722L8etrrWMXgfdxRT5KvJIlDE%2F1Qa7nH4mSMW4mURCkyRoUBCg4d4xul%2B0AvnuVX3FxQq3%2FTTfJZxgSej6N0PfSsRfN6YAw%2F90h0elGXCrTz0i3b%2FKE1AxCHWgYWzB7YTSOeya7COc6qBvTWiTmdnlN85Tso0acoGrWTWI5nqbZKjkHd0TjXKqDLb%2BVHXsrInX8DB%2F7FtONzwbT15gs%2F%2BrvmfGdam2f5rMO6ExW8po5hOSt7RbrzEy0%2Bwb8O1J3e36mJPigzGh1y9F6b95tvMKLQOBK7d8DR0vYERZDAuslREa62R1%2BZFn7L9VX2cQsFMHbLSfrOu5OsFyDnRoVxxiZw0%2BXydMAaMK1xuVP4QsYxUCYg5Arp8x%2FwzAnzhUdMtvZrwkg9QAbXlPSKM79CxvVffvGWTgedEZ6EayxZWs%2FCf1%2Bb07zdGszmd%2Bt4b42xHtnmjm18fJidhhwpXs8YZZIw8r%2FG1QY6pgFS%2BPFRwAIrH3SncrzvkUw8H8VSeDZuoWm2Hin0bashPb9ZyWHQesUybJoYs3gLFgpzoX2QpehcmPCWyAln0QDolqbvv%2BIsxNvlYfvtwcaFkOmFaa6OI7%2F6m2fCH1EZcvzLCpjcmJPjH0I5ozsrUTs0NvEUW%2BP9V%2FdzKpeJBFT44zgS14A5Ky7MysOKGsq%2B6fzArm2J9YeDIjNC78CDVkxXitnTx3bC&X-Amz-Signature=76192ecf57bdcd5ef380e31071348aa44a04acb01ad104d7da2e5c93455e5888&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SKTNCSU%2F20260922%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260922T002045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDSRMNLR%2BDZSM%2FZt%2Bnle04H4G4eLZd%2BZd81wJdznoeEvAiA6uHmHspMDbOtvjWhW2UnDS6sRU8ah9%2FfI3qht9aALGSqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5W72fV4A6yzgRuC6KtwD5sgMGOH86DDoVkzllhb%2BWeDbEcImSwokYJ7bp3%2FwzsiUBH4UMQywkviwGIGW%2FScmHcHu1jTYg%2BrZROBicZImY4QXLh%2Bs33fPg4DOo1fev3KliVIWER0iQgvBCmIrbhIHTcQc0dCiXYHNBrA1hhVWE1OYqiN6h1zafW8722L8etrrWMXgfdxRT5KvJIlDE%2F1Qa7nH4mSMW4mURCkyRoUBCg4d4xul%2B0AvnuVX3FxQq3%2FTTfJZxgSej6N0PfSsRfN6YAw%2F90h0elGXCrTz0i3b%2FKE1AxCHWgYWzB7YTSOeya7COc6qBvTWiTmdnlN85Tso0acoGrWTWI5nqbZKjkHd0TjXKqDLb%2BVHXsrInX8DB%2F7FtONzwbT15gs%2F%2BrvmfGdam2f5rMO6ExW8po5hOSt7RbrzEy0%2Bwb8O1J3e36mJPigzGh1y9F6b95tvMKLQOBK7d8DR0vYERZDAuslREa62R1%2BZFn7L9VX2cQsFMHbLSfrOu5OsFyDnRoVxxiZw0%2BXydMAaMK1xuVP4QsYxUCYg5Arp8x%2FwzAnzhUdMtvZrwkg9QAbXlPSKM79CxvVffvGWTgedEZ6EayxZWs%2FCf1%2Bb07zdGszmd%2Bt4b42xHtnmjm18fJidhhwpXs8YZZIw8r%2FG1QY6pgFS%2BPFRwAIrH3SncrzvkUw8H8VSeDZuoWm2Hin0bashPb9ZyWHQesUybJoYs3gLFgpzoX2QpehcmPCWyAln0QDolqbvv%2BIsxNvlYfvtwcaFkOmFaa6OI7%2F6m2fCH1EZcvzLCpjcmJPjH0I5ozsrUTs0NvEUW%2BP9V%2FdzKpeJBFT44zgS14A5Ky7MysOKGsq%2B6fzArm2J9YeDIjNC78CDVkxXitnTx3bC&X-Amz-Signature=8eb99acf14785f44ae69f38465d5537396464426da2898af1e89d7eaf2af33ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







