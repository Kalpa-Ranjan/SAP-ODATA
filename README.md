



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CB3DAZD%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T014715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQDxKshm%2BRf9Tc2sAjE5ChBXdeXtmtyQ4mahuh1Sq3xWXwIhAMCcEj%2FlTTbuv2oz3ZnC%2FkJonGjb5%2FSuO%2FtznB05E9bVKogECPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwDGReQAm0xc%2B4AUWkq3APpSh%2BkRXYo5xQgCeFD4mjxYWeJYceQVcvDJRe%2BpjNpJJn3Qu%2BaS%2FalNp1gknYRGgLEOWvrB3M6qVn0VAviVG5j23dWF9uI2HNLZkVj%2B8SwT7mhnwvRPK%2BNUZ7pxrAaksz9d9CONgns3OEkioKlCsLqrHtfS%2BpF6PiWNjqRdkxlYoLoH6x9ZQ9VktKHgHqK7bcMYeDZ13oonOJU9U9hcufSmStrguzc0V24f3TMzvQGvXhOQ38HpNmZi%2FXJH2pIWB67frNvQxOl9EuXElqzw8Co6%2F5EcfeYX0lJS0uy8OWPLvB9YHtfOfn%2BHBfTFzBT7VG0wkPVr606YDReWKrhfBU5G4Giic5NVxvzMVHyabUgKvTdeX3pLS16wfZuPfFnC62KTMv82%2FXmOrwLZDGyxgIEbnENMCL%2FNR9hpoSI7TTT9sKqg4ijLLwWNbWondigAgQRmexSWBE37fH92Cs142yQqohSjb6J1YkN5Za1hn1zLNUlIdbmg1%2Fpr2vKWQMRb2xcPFkT38bwIyMRqyYQFewaSFJDEcc7%2FlJJJk53fbq2Hg2JmznEMm2A%2F0JwQ0EBC5F3ZbBR3CTAbZlo3cGwJL2CuClccCCtmIjgHHT2haeR1ZgOsITR92vOZKb41DC3m4XMBjqkATWPsfR3gA8GFJA7vKa3i146gCuyoKQKFaOcs0pboqmr0hOm%2F9V9ILbELGhp6k%2F9cKq5n6QIyLuqfjo%2F1O3k1AS1IqOVWX0RlX%2FYENuVIHE4s4Sbb6rKQBmJMUsAufkZDfjpE5dAQ4MZh5fB9JOs23IQrJK23Hb3ep3wQcoOU02JDUjyGj1kUseXzq1sf7hcEsIA7ZIuIFpGLuOMKlCMRE28rp89&X-Amz-Signature=f4f878ff902dbda5dd78ee2e92ec5c883f44e57510f706e8b0004fe1f1913541&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CB3DAZD%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T014715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQDxKshm%2BRf9Tc2sAjE5ChBXdeXtmtyQ4mahuh1Sq3xWXwIhAMCcEj%2FlTTbuv2oz3ZnC%2FkJonGjb5%2FSuO%2FtznB05E9bVKogECPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwDGReQAm0xc%2B4AUWkq3APpSh%2BkRXYo5xQgCeFD4mjxYWeJYceQVcvDJRe%2BpjNpJJn3Qu%2BaS%2FalNp1gknYRGgLEOWvrB3M6qVn0VAviVG5j23dWF9uI2HNLZkVj%2B8SwT7mhnwvRPK%2BNUZ7pxrAaksz9d9CONgns3OEkioKlCsLqrHtfS%2BpF6PiWNjqRdkxlYoLoH6x9ZQ9VktKHgHqK7bcMYeDZ13oonOJU9U9hcufSmStrguzc0V24f3TMzvQGvXhOQ38HpNmZi%2FXJH2pIWB67frNvQxOl9EuXElqzw8Co6%2F5EcfeYX0lJS0uy8OWPLvB9YHtfOfn%2BHBfTFzBT7VG0wkPVr606YDReWKrhfBU5G4Giic5NVxvzMVHyabUgKvTdeX3pLS16wfZuPfFnC62KTMv82%2FXmOrwLZDGyxgIEbnENMCL%2FNR9hpoSI7TTT9sKqg4ijLLwWNbWondigAgQRmexSWBE37fH92Cs142yQqohSjb6J1YkN5Za1hn1zLNUlIdbmg1%2Fpr2vKWQMRb2xcPFkT38bwIyMRqyYQFewaSFJDEcc7%2FlJJJk53fbq2Hg2JmznEMm2A%2F0JwQ0EBC5F3ZbBR3CTAbZlo3cGwJL2CuClccCCtmIjgHHT2haeR1ZgOsITR92vOZKb41DC3m4XMBjqkATWPsfR3gA8GFJA7vKa3i146gCuyoKQKFaOcs0pboqmr0hOm%2F9V9ILbELGhp6k%2F9cKq5n6QIyLuqfjo%2F1O3k1AS1IqOVWX0RlX%2FYENuVIHE4s4Sbb6rKQBmJMUsAufkZDfjpE5dAQ4MZh5fB9JOs23IQrJK23Hb3ep3wQcoOU02JDUjyGj1kUseXzq1sf7hcEsIA7ZIuIFpGLuOMKlCMRE28rp89&X-Amz-Signature=68c6c0ae0bb05a98034261754c174a3faf96b78fc04b4da2b233e8ec6576ea79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







