



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EALINB7%2F20261128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261128T001158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDaNcP2BVphpgboszoVh6GmqCX9PDUMZEFf71jYYE%2BrIQIhAL5XJuxZlWvodB4CprxjuydcKgwn9CMSOX%2BWX4JHMC8qKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzIjik8bfcxi3LAE7sq3APJKvlQ3r%2F2Nrw989wl0G%2Bd7YnzVzs4A4om2w5EcgD1BnLufZNicIYbRgpiNb1KsW%2B%2BJdnUt3RRC6FdF7uHt4E0Uc950AZNgqyHNGMIq112GdAh1f8l8aqXJ7rAQSil86Dmkgyx66vtuThzodR%2BQQQT%2BzjE2Mrd3n%2FPkrYATs%2FBMB3YEGxZg6Y%2F%2BPcGT2Wb%2FFsKQXhQEx%2B454i%2FGTRWfT53MVikZayvcbrb%2FQxJrJHt4noJ7041vr5Bj1guRT8oQaklMt7QApOCLJxdXxCbeX7ZhNp3k8npCaQCmgs3zlaLb61T6Dicku%2FHCu3cvovY3%2FRzX3lJyZNSaR%2B8F%2BE7IZROw1pgUjzRwRE2LYxkA76s%2B1a6GBi%2FBarpV4dtFJL4p3Ga%2B9Q0G2tJlTrL7JCYD0ZOQYQLyCpAr4jLIgi1McfymXJHLMPvLulTwzmngPLLLn2R06a59Jn4WZtfj9vKm1KjCu2D9V8lUhINqeZrw1MIcD%2FPocAgrx%2FeGrjEJOHxGkbU9YDwpZxl7vDtYtxI4UfeIS8UYdsZGp86swKEjT0nkWcOwY5W1jmwFWjs%2Bxf29wwij78eoB9IjWBXM2ndiw6NtSYBNh3NA3AYywzaCwYJ4f6IwHIgtIpE5dVbPzCKxKfYBjqkAaNcTE%2BnfRhtDdZROKTI6qg5uYGYxuiVBjCNMib8vmiRbjq22%2FVeYb8qKm5q6UVfuJ4jW8b%2FPS%2F73M%2Bz0JTPXQJSALeVUTanT5qS%2Flb48JBSEnZCJ9BRnL6fQXHyEZNVckk2EC9UVMja02D0RBQPiBZoE9K%2B86rhdqFm60yah5QuJCu1wERZWcA26DPlGhUrvR0Z0kTCvbC8N2A4us%2BaTvaS2XYu&X-Amz-Signature=38796c231b78f073c5a9789e9e0377bfdd66d3ae3852bb5f0f7074df3462d0e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EALINB7%2F20261128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261128T001158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDaNcP2BVphpgboszoVh6GmqCX9PDUMZEFf71jYYE%2BrIQIhAL5XJuxZlWvodB4CprxjuydcKgwn9CMSOX%2BWX4JHMC8qKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzIjik8bfcxi3LAE7sq3APJKvlQ3r%2F2Nrw989wl0G%2Bd7YnzVzs4A4om2w5EcgD1BnLufZNicIYbRgpiNb1KsW%2B%2BJdnUt3RRC6FdF7uHt4E0Uc950AZNgqyHNGMIq112GdAh1f8l8aqXJ7rAQSil86Dmkgyx66vtuThzodR%2BQQQT%2BzjE2Mrd3n%2FPkrYATs%2FBMB3YEGxZg6Y%2F%2BPcGT2Wb%2FFsKQXhQEx%2B454i%2FGTRWfT53MVikZayvcbrb%2FQxJrJHt4noJ7041vr5Bj1guRT8oQaklMt7QApOCLJxdXxCbeX7ZhNp3k8npCaQCmgs3zlaLb61T6Dicku%2FHCu3cvovY3%2FRzX3lJyZNSaR%2B8F%2BE7IZROw1pgUjzRwRE2LYxkA76s%2B1a6GBi%2FBarpV4dtFJL4p3Ga%2B9Q0G2tJlTrL7JCYD0ZOQYQLyCpAr4jLIgi1McfymXJHLMPvLulTwzmngPLLLn2R06a59Jn4WZtfj9vKm1KjCu2D9V8lUhINqeZrw1MIcD%2FPocAgrx%2FeGrjEJOHxGkbU9YDwpZxl7vDtYtxI4UfeIS8UYdsZGp86swKEjT0nkWcOwY5W1jmwFWjs%2Bxf29wwij78eoB9IjWBXM2ndiw6NtSYBNh3NA3AYywzaCwYJ4f6IwHIgtIpE5dVbPzCKxKfYBjqkAaNcTE%2BnfRhtDdZROKTI6qg5uYGYxuiVBjCNMib8vmiRbjq22%2FVeYb8qKm5q6UVfuJ4jW8b%2FPS%2F73M%2Bz0JTPXQJSALeVUTanT5qS%2Flb48JBSEnZCJ9BRnL6fQXHyEZNVckk2EC9UVMja02D0RBQPiBZoE9K%2B86rhdqFm60yah5QuJCu1wERZWcA26DPlGhUrvR0Z0kTCvbC8N2A4us%2BaTvaS2XYu&X-Amz-Signature=c05a6c5ffd9cefff36c62fd040eb872e41b7dcc663ebf102c7c7add41701d30a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







