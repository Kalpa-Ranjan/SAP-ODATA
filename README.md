



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKFQPLV5%2F20260619%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260619T034839Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBS6cNMomO3suLz9sEW48l7CG8grA4r%2BhTfL3LsAEFLrAiB47%2B9tURDMGF5gpZUB0%2FbQHMaIESbptKeBqAkRys4NoSqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMB86eoWc9pajN0pmgKtwDaW4AtoUu%2B8bmGnz5b3D%2FRHLN1BAhng4h%2F8VuaBHoc7x5Ww0yokofVt1XaQHPAcCzUQgJfldaw9%2BljtHXLHT6xNNJC25PiCUqjwpwjKgh0va%2Bu2WU5TqqIoFOe%2B%2BVXtL%2Fhh5Otqynoa9ODnm2r5cNjzfZiFApe1ElaFx6pSQdnGFc1Q0x5AUcCkZcgp%2FtcR3RwqtDQwUnHEQI%2FDfne6NDH0fHWngB%2FcpfQJF4TzD5r52LaEkO9dnNkh3U%2FOFmZ9y16WPdgHUv4lanjagBvvgVtFH8ER3kaqJyEPjOF6feuVcRYdmcsbW1tvekxRTAcni8%2BAagF%2FTV5QKMUCmXPGftxcndHde6K0WLQpIcAZUU34HoQlsmVEJORyaIcS6qS5NFrmZUALqlQnPF4qc7BknlyOBa8wQUekzyEDWiiSDdC4q3HIZO14IgDHR3bOZRIfRBrjYCwW6yCk6kZS2LMT4zDzlc0H1AT4oGGPSRdKaukK8sH1pOH5VYi1drNtXRk9vbjzEFCueRRxEqIOQq4JOJO8%2FdIO16ESZ7RQBx64SD8bM5%2FWCfKeWehc%2Fgm7XtDI8rejL7xfIbx8g4iLexoRLTlsrFsdMJ%2Bt3K%2BZKeADES6q0Tv44j7rkjGfZ0uo8wwqHS0QY6pgHKhozZXAJK51AAiO0zISVzMWTJ9QjLzX1LU4ydToU3yx0dOG3%2BSgUW46tacOFeUG2D09dNUpiecR7mUxMmshu9%2BGSNzhiLrRSzTyEP%2F40fSDsfI0oG5jQHEkn5%2F00ddFddDXU%2B%2Fhj%2BuW6cItHp57vIuIDJMBjf0ICnGj7C7VOFhSc5nKrG67Pf0nQCweowdEVR36w0S3YurumpoAJDcKziyCQoKQwP&X-Amz-Signature=475af8fd7fe899e181267077ebfb98bef72a0b002e68d91360bf97840753ad77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKFQPLV5%2F20260619%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260619T034839Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBS6cNMomO3suLz9sEW48l7CG8grA4r%2BhTfL3LsAEFLrAiB47%2B9tURDMGF5gpZUB0%2FbQHMaIESbptKeBqAkRys4NoSqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMB86eoWc9pajN0pmgKtwDaW4AtoUu%2B8bmGnz5b3D%2FRHLN1BAhng4h%2F8VuaBHoc7x5Ww0yokofVt1XaQHPAcCzUQgJfldaw9%2BljtHXLHT6xNNJC25PiCUqjwpwjKgh0va%2Bu2WU5TqqIoFOe%2B%2BVXtL%2Fhh5Otqynoa9ODnm2r5cNjzfZiFApe1ElaFx6pSQdnGFc1Q0x5AUcCkZcgp%2FtcR3RwqtDQwUnHEQI%2FDfne6NDH0fHWngB%2FcpfQJF4TzD5r52LaEkO9dnNkh3U%2FOFmZ9y16WPdgHUv4lanjagBvvgVtFH8ER3kaqJyEPjOF6feuVcRYdmcsbW1tvekxRTAcni8%2BAagF%2FTV5QKMUCmXPGftxcndHde6K0WLQpIcAZUU34HoQlsmVEJORyaIcS6qS5NFrmZUALqlQnPF4qc7BknlyOBa8wQUekzyEDWiiSDdC4q3HIZO14IgDHR3bOZRIfRBrjYCwW6yCk6kZS2LMT4zDzlc0H1AT4oGGPSRdKaukK8sH1pOH5VYi1drNtXRk9vbjzEFCueRRxEqIOQq4JOJO8%2FdIO16ESZ7RQBx64SD8bM5%2FWCfKeWehc%2Fgm7XtDI8rejL7xfIbx8g4iLexoRLTlsrFsdMJ%2Bt3K%2BZKeADES6q0Tv44j7rkjGfZ0uo8wwqHS0QY6pgHKhozZXAJK51AAiO0zISVzMWTJ9QjLzX1LU4ydToU3yx0dOG3%2BSgUW46tacOFeUG2D09dNUpiecR7mUxMmshu9%2BGSNzhiLrRSzTyEP%2F40fSDsfI0oG5jQHEkn5%2F00ddFddDXU%2B%2Fhj%2BuW6cItHp57vIuIDJMBjf0ICnGj7C7VOFhSc5nKrG67Pf0nQCweowdEVR36w0S3YurumpoAJDcKziyCQoKQwP&X-Amz-Signature=86d971a41d10f872e2799c94a3659a7e1e526a2e61c6e9c1487e1f7a64ad0f18&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







