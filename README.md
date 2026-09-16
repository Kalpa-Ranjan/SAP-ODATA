



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AA75D5X%2F20260916%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260916T061327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQC4GtoxlsKADBBMtSzWcvD1JUWMeEmaPe3yICP3qP7E5AIhAKrQ0d2NnRcyzUgVgRwtGkvkhlT45gJp9yJsqQw0f37mKv8DCA8QABoMNjM3NDIzMTgzODA1IgzsDdGzKVJ0R8ZmcUsq3AMqeA8NH1tH2Oy4YFsIRJdw%2BCmzS67Cb7iZRH96ltN5gusc3Qrn5sVY4QWakXnsrk8QdaYf4THzckKZELYwzKfY%2F%2Fcf1JS6wfsj3V%2BFMOFIoO4RqXFtRDv9CU%2BJuwYKR2A5APSe4e4w3BxW7YqJb2Ps7dG5DEp2I%2B49diaSBjGFZYCAHsO1ug%2FoaB952sdanibv98PbVSGBeIQNa0yNYvGxNe3kBQJ07MrPrGDqZ9uTM8hZwINgCcYmLldKFC2qiGUzWi9tMqvyspjcbo3RgQNOgudD%2FVe2TOMy0hTATa0NThkfV5sezA2LaDi2uLH7VPYc42skllgDjipLKl8UCWFAHymED5iO%2BRKuZY9G2%2BWcP5HqyliX%2FYVdtb8Hn3xbPGaWDhggg25PH%2FpfkcgPGI%2BqonTCym%2B2TFhTKzQ5wkVzG5ZAR2%2FJlKdEUBVotgbf2X6E0t5HHX7MxZYu4E6EaHA4gpekO4INPhzekR%2B4%2Feu%2F7Zw3W7zeU0I2uFfOZhWYfpvdcNNObTH5CrYzHvrVfHsuRpkGE29T%2B8oQOOgOzyVqZniIzCQNY16vrxGYtsTieH%2B4JwGbLN1OXLoDHIX%2BNqIc0zzCc1UFI4tYs5Y7WTfeFQz1klOz3qtSy66ZEDCE3KjVBjqkAWqjzUTlQ0prplpR%2Bop9mkulaH3d3NCOywyrYqM9RA9y3bh5MMcIDRqhOAeCGy0Zm%2FguahFNA5LhCq1M3LIwpbUPD0jTdoRoEFDq08qEc8qV4dW8J0GSNtBdjZf62FP8DqvHj7pH53cy%2Bw54VP4P2yDQswcUcUW94iPyb3xF%2F9VmytBb4mNqYPWmt2UXsqzwegyGJE9p3tkoxWGZUrQ541zd2DS3&X-Amz-Signature=b2df0d0aaf7e198f0e8ded8ff60d687983e0970d41317e927ecda4eadd233ce3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AA75D5X%2F20260916%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260916T061327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQC4GtoxlsKADBBMtSzWcvD1JUWMeEmaPe3yICP3qP7E5AIhAKrQ0d2NnRcyzUgVgRwtGkvkhlT45gJp9yJsqQw0f37mKv8DCA8QABoMNjM3NDIzMTgzODA1IgzsDdGzKVJ0R8ZmcUsq3AMqeA8NH1tH2Oy4YFsIRJdw%2BCmzS67Cb7iZRH96ltN5gusc3Qrn5sVY4QWakXnsrk8QdaYf4THzckKZELYwzKfY%2F%2Fcf1JS6wfsj3V%2BFMOFIoO4RqXFtRDv9CU%2BJuwYKR2A5APSe4e4w3BxW7YqJb2Ps7dG5DEp2I%2B49diaSBjGFZYCAHsO1ug%2FoaB952sdanibv98PbVSGBeIQNa0yNYvGxNe3kBQJ07MrPrGDqZ9uTM8hZwINgCcYmLldKFC2qiGUzWi9tMqvyspjcbo3RgQNOgudD%2FVe2TOMy0hTATa0NThkfV5sezA2LaDi2uLH7VPYc42skllgDjipLKl8UCWFAHymED5iO%2BRKuZY9G2%2BWcP5HqyliX%2FYVdtb8Hn3xbPGaWDhggg25PH%2FpfkcgPGI%2BqonTCym%2B2TFhTKzQ5wkVzG5ZAR2%2FJlKdEUBVotgbf2X6E0t5HHX7MxZYu4E6EaHA4gpekO4INPhzekR%2B4%2Feu%2F7Zw3W7zeU0I2uFfOZhWYfpvdcNNObTH5CrYzHvrVfHsuRpkGE29T%2B8oQOOgOzyVqZniIzCQNY16vrxGYtsTieH%2B4JwGbLN1OXLoDHIX%2BNqIc0zzCc1UFI4tYs5Y7WTfeFQz1klOz3qtSy66ZEDCE3KjVBjqkAWqjzUTlQ0prplpR%2Bop9mkulaH3d3NCOywyrYqM9RA9y3bh5MMcIDRqhOAeCGy0Zm%2FguahFNA5LhCq1M3LIwpbUPD0jTdoRoEFDq08qEc8qV4dW8J0GSNtBdjZf62FP8DqvHj7pH53cy%2Bw54VP4P2yDQswcUcUW94iPyb3xF%2F9VmytBb4mNqYPWmt2UXsqzwegyGJE9p3tkoxWGZUrQ541zd2DS3&X-Amz-Signature=1d8bfd22324625806cca91c3c69d80dbf5c09473fc09816669d5f932c01a93ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







