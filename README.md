



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UC52GIAB%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T130742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIAhC5dwjxV3bfWbyTHwF%2FR%2FC4%2FRbkSGR3seJwW%2F4qVJ3AiEA22W0%2FJhgTE41ik7Sv8KCPmfVrkXFXUaUSu3LErW3vNgq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDBL%2BBjSaBrO7sQS25ircA%2B3TQk58pRtn68GiocsCYpKNWw%2FQrDC0JzOwKaSBv7Tdj4s5hd0sssjaTE6BPFK5YvkX7gkB3vc1jx8f7u9QDYbiGlji45IYPiYqLaNyA20NfBYG5LzmElOSjUJWyrb9IpVe9YNBZguqlZIAPnC9I0oEdHOaBihVWErplz0%2Bo45t%2BLLR7T6t3eP6ksqgEF4b3WwJkDQKBd%2BWhTIfATYFhDzp%2FJp8WXJd4c9LfvNQawtWLhQa%2FcaF1QOoSdXhMRkv3I%2FhmmRO%2FZh9zXoUtJSiIG0LDUD519a9JQiEGQHVwB9t9msMc%2BfQE0E%2FyrAh4vGRXDJA9ZhJ%2BdoMh3vYvTLkFjYj9Jpi%2FvsROaCufu1f7dJw5efkt3bONRinGwHn7K%2BFPdToOsc0yB3AmysoI4X4rgs7St%2BnzEOu8BfICxxUcqwTTxMe2yiu1LYOnvHic2wqxM4ULB2sWQ5cDTQuJ8PmkI0Pgz1LRKHYQuLtrDdhHeuOkQFLG9CsR2dvTQWicYysnjbEwdD5l46a1uE6PKtK0J7hvc%2FoHz3LIFd6WNSMIJnwtpRHbu%2BgU7IdF6hZbTuOXnpw5JwMy5U%2F25Oe%2F9L0bUDTMFcQIFyutGd7iCi8uof7%2B95rQZSwWME5DjgKMObBqc4GOqUB0LVZEWbVWG6hBpynLwSzF18RlqHPbqaNRzDgAJW9IWRWnWiPUW8sKwNkSyvzFoePFQABHF7L5wzSnAX7lAsQkBIlpnDbACkWwG1V%2BbQqeLehMSYGECeT2BmzU9KXPYDJIVOsXze0HvcdQfP%2FXrKP8zJQ39O9oo1koM1dMpHUO3eeDvaO6QjZMIOwbF%2BrZZtH541dXhBAlafahPx8YtPmlcy%2BxRel&X-Amz-Signature=2e723f0737110d83eba966937449a95189f3779ee3da4a358b07e06c993d91e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UC52GIAB%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T130743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIAhC5dwjxV3bfWbyTHwF%2FR%2FC4%2FRbkSGR3seJwW%2F4qVJ3AiEA22W0%2FJhgTE41ik7Sv8KCPmfVrkXFXUaUSu3LErW3vNgq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDBL%2BBjSaBrO7sQS25ircA%2B3TQk58pRtn68GiocsCYpKNWw%2FQrDC0JzOwKaSBv7Tdj4s5hd0sssjaTE6BPFK5YvkX7gkB3vc1jx8f7u9QDYbiGlji45IYPiYqLaNyA20NfBYG5LzmElOSjUJWyrb9IpVe9YNBZguqlZIAPnC9I0oEdHOaBihVWErplz0%2Bo45t%2BLLR7T6t3eP6ksqgEF4b3WwJkDQKBd%2BWhTIfATYFhDzp%2FJp8WXJd4c9LfvNQawtWLhQa%2FcaF1QOoSdXhMRkv3I%2FhmmRO%2FZh9zXoUtJSiIG0LDUD519a9JQiEGQHVwB9t9msMc%2BfQE0E%2FyrAh4vGRXDJA9ZhJ%2BdoMh3vYvTLkFjYj9Jpi%2FvsROaCufu1f7dJw5efkt3bONRinGwHn7K%2BFPdToOsc0yB3AmysoI4X4rgs7St%2BnzEOu8BfICxxUcqwTTxMe2yiu1LYOnvHic2wqxM4ULB2sWQ5cDTQuJ8PmkI0Pgz1LRKHYQuLtrDdhHeuOkQFLG9CsR2dvTQWicYysnjbEwdD5l46a1uE6PKtK0J7hvc%2FoHz3LIFd6WNSMIJnwtpRHbu%2BgU7IdF6hZbTuOXnpw5JwMy5U%2F25Oe%2F9L0bUDTMFcQIFyutGd7iCi8uof7%2B95rQZSwWME5DjgKMObBqc4GOqUB0LVZEWbVWG6hBpynLwSzF18RlqHPbqaNRzDgAJW9IWRWnWiPUW8sKwNkSyvzFoePFQABHF7L5wzSnAX7lAsQkBIlpnDbACkWwG1V%2BbQqeLehMSYGECeT2BmzU9KXPYDJIVOsXze0HvcdQfP%2FXrKP8zJQ39O9oo1koM1dMpHUO3eeDvaO6QjZMIOwbF%2BrZZtH541dXhBAlafahPx8YtPmlcy%2BxRel&X-Amz-Signature=b822d71b91086c39eb415459878093926d3461982c10bee87c1fccdac90f42be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







