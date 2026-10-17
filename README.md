



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVPFRK5S%2F20261017%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261017T061053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC0aCXVzLXdlc3QtMiJHMEUCIBPN3U0OtFj%2BlbFZiJ0RttuZ98U7RFVkkyREG31A4j42AiEA6oWlku4DVaMCHm72ZL%2FiCL566ATQraypIHTjW1ia%2FHUqiAQI9v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHLGd4dX55y%2FI2Zx6CrcAwIDUqbNwulMbFJ3LXhX9kaLrO2OAYNMkCsQcJurfH9%2FkjNVsBRcNi4iklfSpScU9N15gsisCTrMzBsYq2fY%2FC9062JSd0Tt%2B89lvFELghiTYZVNDx2ukJODkf5EVeDrRNZ1pK7cYNs9GuAzW%2FfdP7gHCOad92pSNMARQhoC%2F%2F7DbiDguhpd%2Bb33GROfb5r2cLyYVdPrOVMb6v3Gih%2FXM5JdQF9AEQow5LEdH40XO%2FQGcwD0UAp1jj7zAM182VwYi6fS3R1y%2F6RuFwAqSSKbcBFztKxYRGbdWaFKdY7usXYegqB%2BOeeVZ%2BR6UEGVtM7X75hOsApnaueubDwSPInZ%2BI7J7lv9ICelVDSPudRWrEOVb7k9bvLouhJEWm0VyYoRLhFKHtojnF0ga%2BfNXXFnC%2BCMiaP5zXnbTp8ioNv3iwC3ZiewTlrCYe%2BWsItIzJCeAI6V5CblU07Q0uHN1BG1KRDjylVeFS4AI0aHeE0OEiMm6OUHY6Bt%2BRUjT0Z9fOFhsbtIGcME7XNQO8L1d0RmePNr5POcOgLETpIANu1QCSek%2BVIb1nDCFKagCnYVGZhYcn1p37xK3uTHPU44mfrV1YKfKHspeVEcO3BZfLv1b%2BS%2FseEYiNjlGwfnobwlMPqIzNYGOqUBVu%2BW21%2B%2BhpAUP2WRLxvw29s97ptqmvQHIfS%2FdMc5ODGDAdkxhQCaS0B4fpnGcrtxKI%2Fc5jjOv0SixZF4X5wPoBL048pzx1DA4FClcllzECJto8FKWOCOhOz0USXbi7E33GIXDGEIM2CdbToiv95uDBZd%2FzPyhfHi5mpIobOijkQwpvp4KVJPEsQz3A3zuwD6B4fTVEL%2F7XmdKrs5eidCNt9qyqnD&X-Amz-Signature=43f6724dfadf707b2fd8d962a1795f17e0b6678e439cfe413d27ebbef9a05444&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVPFRK5S%2F20261017%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261017T061054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC0aCXVzLXdlc3QtMiJHMEUCIBPN3U0OtFj%2BlbFZiJ0RttuZ98U7RFVkkyREG31A4j42AiEA6oWlku4DVaMCHm72ZL%2FiCL566ATQraypIHTjW1ia%2FHUqiAQI9v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHLGd4dX55y%2FI2Zx6CrcAwIDUqbNwulMbFJ3LXhX9kaLrO2OAYNMkCsQcJurfH9%2FkjNVsBRcNi4iklfSpScU9N15gsisCTrMzBsYq2fY%2FC9062JSd0Tt%2B89lvFELghiTYZVNDx2ukJODkf5EVeDrRNZ1pK7cYNs9GuAzW%2FfdP7gHCOad92pSNMARQhoC%2F%2F7DbiDguhpd%2Bb33GROfb5r2cLyYVdPrOVMb6v3Gih%2FXM5JdQF9AEQow5LEdH40XO%2FQGcwD0UAp1jj7zAM182VwYi6fS3R1y%2F6RuFwAqSSKbcBFztKxYRGbdWaFKdY7usXYegqB%2BOeeVZ%2BR6UEGVtM7X75hOsApnaueubDwSPInZ%2BI7J7lv9ICelVDSPudRWrEOVb7k9bvLouhJEWm0VyYoRLhFKHtojnF0ga%2BfNXXFnC%2BCMiaP5zXnbTp8ioNv3iwC3ZiewTlrCYe%2BWsItIzJCeAI6V5CblU07Q0uHN1BG1KRDjylVeFS4AI0aHeE0OEiMm6OUHY6Bt%2BRUjT0Z9fOFhsbtIGcME7XNQO8L1d0RmePNr5POcOgLETpIANu1QCSek%2BVIb1nDCFKagCnYVGZhYcn1p37xK3uTHPU44mfrV1YKfKHspeVEcO3BZfLv1b%2BS%2FseEYiNjlGwfnobwlMPqIzNYGOqUBVu%2BW21%2B%2BhpAUP2WRLxvw29s97ptqmvQHIfS%2FdMc5ODGDAdkxhQCaS0B4fpnGcrtxKI%2Fc5jjOv0SixZF4X5wPoBL048pzx1DA4FClcllzECJto8FKWOCOhOz0USXbi7E33GIXDGEIM2CdbToiv95uDBZd%2FzPyhfHi5mpIobOijkQwpvp4KVJPEsQz3A3zuwD6B4fTVEL%2F7XmdKrs5eidCNt9qyqnD&X-Amz-Signature=238bbf0a5e78ab1fe73a3998d8e5e223e1ab14bbe30052adc84ee7d44d5b4635&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







