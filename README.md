



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IDMMZL7%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T071008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQDDCnWMDouL7KdwWx6z3qzM0%2FCok0YEXgNjbU8RWUfWywIgdfY0yiJ6Zlk14H6d69Pc7jifphYF14UIMMJmrZXAqNUqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEY7PkQ%2FKDKXsobszSrcA1a9d4UnCoanCRkHde2IQnp22zlY81mXEYCzRJVDIQvEia5SP%2BLA3DJmpWke2RwwKQ75p8MMQuLtOF4%2BB8pXTLzaFouz9jjeTptTtY6ECYD9lPfEYEbMWmyNIBWqU03W42I9RbW7GOAOvid5QW7rGzAc%2FmSfbYiImPt4aZCFwSBvl8izNEf3mXC10DcnZEOhe46dpjUj7wFADqmYsJckTTqaXBYttXwPU5JR72LJpQ0F7khNoUJ6bscF3VqR027XUc0B%2F7W5YeTJWrgNOsy%2BuLNT%2BJIwS3XsSCViEVEN6mfCIFc5k%2FaYs5SsCLSQQNP%2Frpm8sr3xlmas0PJAP5Z8KpljTIMoA163NJQIJVkubzFJMP8pZWGvLPG%2BIByF5iKhMEVE6VtPRfVfU2aq1bbWOjzvahqtSY1eVqcbhM113H0NuO9xRLg6mQXCz%2BexJV68OOylU9lOynisF9savwuI37U018HB9MdDcLkMy8rpkPgBOiC9oU73Z4TJE1aE9DKmH5q%2F%2Ff9a69o%2BJyAGg2Ip8hM5ivDjPKr0Ldo22OU7VyKJqK8upv%2B2hZ3uwiVVDDnloCR1zrsXegTx91f09QC53aUx%2BV%2FGMipKfrwOFxXUA%2FAK0BXgP3VGv%2BP9OujUMK%2BJ3s0GOqUByV%2FWV5imaynIIp8s94ia0vcl6O9axPPg2reTnSnso995eTw6ZH%2BVLfsPSUCcFKPsm%2F%2F9W2tVgNP9G8eB33L1clIlQeTN0liNb7ULQZJmbe4ZmvkBCgbYhSK%2FYiU7Vn%2BrT7408yIlXUt4zFXx9XNe3%2BrW9kC4glzc2bqxvAp26me2bbk%2Bp7HYTTKQUidQiBnZwgD%2B8YNKWfMgAnAYLEIq4YyNQTwQ&X-Amz-Signature=90f4cecb86be8c96c90e6b53f620f7294b3cdd82807893bdf3ab4ade5327510e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IDMMZL7%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T071008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQDDCnWMDouL7KdwWx6z3qzM0%2FCok0YEXgNjbU8RWUfWywIgdfY0yiJ6Zlk14H6d69Pc7jifphYF14UIMMJmrZXAqNUqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEY7PkQ%2FKDKXsobszSrcA1a9d4UnCoanCRkHde2IQnp22zlY81mXEYCzRJVDIQvEia5SP%2BLA3DJmpWke2RwwKQ75p8MMQuLtOF4%2BB8pXTLzaFouz9jjeTptTtY6ECYD9lPfEYEbMWmyNIBWqU03W42I9RbW7GOAOvid5QW7rGzAc%2FmSfbYiImPt4aZCFwSBvl8izNEf3mXC10DcnZEOhe46dpjUj7wFADqmYsJckTTqaXBYttXwPU5JR72LJpQ0F7khNoUJ6bscF3VqR027XUc0B%2F7W5YeTJWrgNOsy%2BuLNT%2BJIwS3XsSCViEVEN6mfCIFc5k%2FaYs5SsCLSQQNP%2Frpm8sr3xlmas0PJAP5Z8KpljTIMoA163NJQIJVkubzFJMP8pZWGvLPG%2BIByF5iKhMEVE6VtPRfVfU2aq1bbWOjzvahqtSY1eVqcbhM113H0NuO9xRLg6mQXCz%2BexJV68OOylU9lOynisF9savwuI37U018HB9MdDcLkMy8rpkPgBOiC9oU73Z4TJE1aE9DKmH5q%2F%2Ff9a69o%2BJyAGg2Ip8hM5ivDjPKr0Ldo22OU7VyKJqK8upv%2B2hZ3uwiVVDDnloCR1zrsXegTx91f09QC53aUx%2BV%2FGMipKfrwOFxXUA%2FAK0BXgP3VGv%2BP9OujUMK%2BJ3s0GOqUByV%2FWV5imaynIIp8s94ia0vcl6O9axPPg2reTnSnso995eTw6ZH%2BVLfsPSUCcFKPsm%2F%2F9W2tVgNP9G8eB33L1clIlQeTN0liNb7ULQZJmbe4ZmvkBCgbYhSK%2FYiU7Vn%2BrT7408yIlXUt4zFXx9XNe3%2BrW9kC4glzc2bqxvAp26me2bbk%2Bp7HYTTKQUidQiBnZwgD%2B8YNKWfMgAnAYLEIq4YyNQTwQ&X-Amz-Signature=c5863fa3a2e06e3c9e29bdffba2b9bd1db15bb37933752c8a649a4408485c253&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







