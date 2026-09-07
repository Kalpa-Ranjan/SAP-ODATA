



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WNDK6V2%2F20260907%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260907T002241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJIMEYCIQDocy8heQLi%2BQR%2Ftyad%2B86Fc2bBHWoIJ3dH%2BsacMk4PngIhAMXw2TPV%2BGEkqnBv7i0UB9CKsbaNv1wBje1Y3yQGPvJsKv8DCDAQABoMNjM3NDIzMTgzODA1IgwwuonKI%2FFLglOcxJ8q3AOfIPHdPcT2N%2FIF3EqFzerMB47VuhC1%2F624BD36HJjuymOKQ7RzxiETBMUftmNaSaxjnUthgaMEPwuddZi6RUtB%2FLYWHbeHOPTo9DyVJ6kjcqKYUQONIQkDIl2wYBw59K91gPdmm4UzcnFWLjpsMSFJpxkrHC%2FMM6EPRLyWBeQ5ekPzBOUlGh%2Fc0tzEHhRIlo5AHT36AYZkJ%2Bk9HZ81knpIk9%2BoVpqRSYKj%2Bh%2BRp7XTT4Vr05l08ropwuNLwMrIsidpU%2B21A%2B99ZvnoLuqnINREhmi071%2BopZy11yxmyOUHKbApMxfEDY7Uiw44kT4a8RG0TOKl0dhxgVjKpXGfJecTijLS73lJ1%2F9Odp85LDU4yzGevoSYuutsW6TkNrmD8RLuD66ebM%2FykT9Cb%2FYBsX2G7%2B%2BnNlrvSHef9wmtEQxy0NmYaGOk7f5sUS4o7Oq0NHeajy6YGQM3fW7JxsA8f%2B2w62NdWPIk%2FPmsyPYazVYN6Ked8Udl8WEp9WLtfYECNtFDIdXfi37Hv30wtb2ml4KSn2FG7GzztlU04oy%2Bo6ETIGfPZnllcZIObbEt4rc1tHFJKmx%2FHC3B5h%2Fqodr3uq%2FqMXn01XPoDZUQa2fZK754H7IjATs3rZ3L8ZNNkzC81%2FfUBjqkAYG11SnPvRYOnWGvR0ITHbVeufYEd95QEItsMEMDWVCPh1N2uueviZbjHgfNwoYOI71G7Gal1g3%2BYKkpP0A6YyFjEJ6Ruyb%2FCd8sEHIztZx5HPky7yKO1nka%2BeyTL1sdg%2BCB4%2BiKp0%2FDUkIsXF0uNW4P3I4J1f6xyjJjjrjasyJBgOMmbavQAAlaFfuXSQsj8U6EYDNPqsXaZLycMtmaNgduTdTB&X-Amz-Signature=bb973159e321b7c970eb5c38f6303bfb8abef16395f7cb6b7eb09042c24c5979&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WNDK6V2%2F20260907%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260907T002241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJIMEYCIQDocy8heQLi%2BQR%2Ftyad%2B86Fc2bBHWoIJ3dH%2BsacMk4PngIhAMXw2TPV%2BGEkqnBv7i0UB9CKsbaNv1wBje1Y3yQGPvJsKv8DCDAQABoMNjM3NDIzMTgzODA1IgwwuonKI%2FFLglOcxJ8q3AOfIPHdPcT2N%2FIF3EqFzerMB47VuhC1%2F624BD36HJjuymOKQ7RzxiETBMUftmNaSaxjnUthgaMEPwuddZi6RUtB%2FLYWHbeHOPTo9DyVJ6kjcqKYUQONIQkDIl2wYBw59K91gPdmm4UzcnFWLjpsMSFJpxkrHC%2FMM6EPRLyWBeQ5ekPzBOUlGh%2Fc0tzEHhRIlo5AHT36AYZkJ%2Bk9HZ81knpIk9%2BoVpqRSYKj%2Bh%2BRp7XTT4Vr05l08ropwuNLwMrIsidpU%2B21A%2B99ZvnoLuqnINREhmi071%2BopZy11yxmyOUHKbApMxfEDY7Uiw44kT4a8RG0TOKl0dhxgVjKpXGfJecTijLS73lJ1%2F9Odp85LDU4yzGevoSYuutsW6TkNrmD8RLuD66ebM%2FykT9Cb%2FYBsX2G7%2B%2BnNlrvSHef9wmtEQxy0NmYaGOk7f5sUS4o7Oq0NHeajy6YGQM3fW7JxsA8f%2B2w62NdWPIk%2FPmsyPYazVYN6Ked8Udl8WEp9WLtfYECNtFDIdXfi37Hv30wtb2ml4KSn2FG7GzztlU04oy%2Bo6ETIGfPZnllcZIObbEt4rc1tHFJKmx%2FHC3B5h%2Fqodr3uq%2FqMXn01XPoDZUQa2fZK754H7IjATs3rZ3L8ZNNkzC81%2FfUBjqkAYG11SnPvRYOnWGvR0ITHbVeufYEd95QEItsMEMDWVCPh1N2uueviZbjHgfNwoYOI71G7Gal1g3%2BYKkpP0A6YyFjEJ6Ruyb%2FCd8sEHIztZx5HPky7yKO1nka%2BeyTL1sdg%2BCB4%2BiKp0%2FDUkIsXF0uNW4P3I4J1f6xyjJjjrjasyJBgOMmbavQAAlaFfuXSQsj8U6EYDNPqsXaZLycMtmaNgduTdTB&X-Amz-Signature=f1dbebc2c86e4ccd753ba080dd0e86d41bf8ef1acdb69c314084afc042a15294&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







