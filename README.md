



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4MSS2LO%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T122936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDLt%2BWq75mSG%2BDLKugc5j%2BQqNdjovNFqA6F1yXzWljQugIhALpbkEc06tbEM6vVs%2F9fLE2amTOxvqA89hLshHIB0VbgKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyzsyf0qDRffRG317gq3AP1FtLTSYeNisEjIXeZgmeoCXDSJyrHbk1BPSA5ZV9hSZ%2F9ovkJ%2FjLXNoOW1nVZxhStjpbJD2wA%2Bhk3FgGXjcPJWafLb4F5Wr3HDxTdC7dpJ8NCag5ZCO%2BNfqHgYVuyNAw%2FN22i8TCKDFIFYnsgVAYZTd9VB9L%2F0Fn%2Fb4WPElrVXO%2Blm%2Bh0gfxsoKHGksvjsJVN5SALRpAhyIj10YJGyNpL7pscgTcAsbChiAsTkcbAT%2FtioN0SZIGPbrO6eGeSyWz1%2BO8gwLy7FJKaYN2my4tSXckqTvbJ9aEKgEz9GKiDx3A0oC1pb5lYx4zzeVue5XV6eV8Iv4SV5S7i0oGV3c%2BO0Fd2rSQ8JSY7Hk6v4ImySweihlStn7W7FILkYC%2FzNgmY%2BEVpkBKTODlxzCqz7vwCrPY773R9TKTYGNVHEimpZmDkJo251yHpHzv42%2BiFQbeq64bn9f3fw8PcsWv3cleOVZe8TXnhemZwOZQ%2BpCQwvBJV122UPsIMmayHICeJ3mAItS1wnN2LTByMgZh759PFyF684V5Eud9fzDTN4aIauln%2F1fc3iV2V496sE16dnpdaS9aCAkllBZoixYbjocohn%2FYHBdx7MqK4amk77htTo1EwSuhlvBwqUdhE6TDnkKvJBjqkARmKL%2F2p4BPsqMnUKDTCFLC%2FxjivtelUl5XHBUU6y91n%2FdKeuFYEtJEh613btlEJtliqCgm%2BoynzlK5%2B9rYLmUKZmU%2BawnV6sUl9V%2Bj5hYog%2BXprocvGkpWi%2BIfeP7amswDyxeFZylTa2isEnEgOWpPbGd1gxtitUu1stJ61oW94cIHPEmtSOLra9IPQpo4xvvdDhOXphW4dZ0IxeCpa0t%2F67Ocp&X-Amz-Signature=3ff627adefb62b7c5a96e43bb676533373ccc6b0adcbf73530dd62cf35ee7d97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4MSS2LO%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T122937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDLt%2BWq75mSG%2BDLKugc5j%2BQqNdjovNFqA6F1yXzWljQugIhALpbkEc06tbEM6vVs%2F9fLE2amTOxvqA89hLshHIB0VbgKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyzsyf0qDRffRG317gq3AP1FtLTSYeNisEjIXeZgmeoCXDSJyrHbk1BPSA5ZV9hSZ%2F9ovkJ%2FjLXNoOW1nVZxhStjpbJD2wA%2Bhk3FgGXjcPJWafLb4F5Wr3HDxTdC7dpJ8NCag5ZCO%2BNfqHgYVuyNAw%2FN22i8TCKDFIFYnsgVAYZTd9VB9L%2F0Fn%2Fb4WPElrVXO%2Blm%2Bh0gfxsoKHGksvjsJVN5SALRpAhyIj10YJGyNpL7pscgTcAsbChiAsTkcbAT%2FtioN0SZIGPbrO6eGeSyWz1%2BO8gwLy7FJKaYN2my4tSXckqTvbJ9aEKgEz9GKiDx3A0oC1pb5lYx4zzeVue5XV6eV8Iv4SV5S7i0oGV3c%2BO0Fd2rSQ8JSY7Hk6v4ImySweihlStn7W7FILkYC%2FzNgmY%2BEVpkBKTODlxzCqz7vwCrPY773R9TKTYGNVHEimpZmDkJo251yHpHzv42%2BiFQbeq64bn9f3fw8PcsWv3cleOVZe8TXnhemZwOZQ%2BpCQwvBJV122UPsIMmayHICeJ3mAItS1wnN2LTByMgZh759PFyF684V5Eud9fzDTN4aIauln%2F1fc3iV2V496sE16dnpdaS9aCAkllBZoixYbjocohn%2FYHBdx7MqK4amk77htTo1EwSuhlvBwqUdhE6TDnkKvJBjqkARmKL%2F2p4BPsqMnUKDTCFLC%2FxjivtelUl5XHBUU6y91n%2FdKeuFYEtJEh613btlEJtliqCgm%2BoynzlK5%2B9rYLmUKZmU%2BawnV6sUl9V%2Bj5hYog%2BXprocvGkpWi%2BIfeP7amswDyxeFZylTa2isEnEgOWpPbGd1gxtitUu1stJ61oW94cIHPEmtSOLra9IPQpo4xvvdDhOXphW4dZ0IxeCpa0t%2F67Ocp&X-Amz-Signature=be8c113c72cafd1c22a65267c473601ae80d311192e7882f385ce8d37f89058b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







