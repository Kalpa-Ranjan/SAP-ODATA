



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RCOFMAG%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T142019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFOAqNeQXQ9rYaZjZkvmWwO0Kbc7bfHOIyAeiY13x5uPAiEAtsJetJC5ctr3271iDxdBPoY%2BlqFb0VkXeQ3z0p7Jg6Mq%2FwMIThAAGgw2Mzc0MjMxODM4MDUiDBjXGgCawbm2NujaiircA8cAg57HdI%2Bhe3jnq8HIxGaoqXL2ehahNY8F5eboIC7XkFs7PazBNb9THv4Pk%2Buf6gc5qi50GbCh%2FGTXFLdkT0%2Bjoy9IRXb7JHg9UDkQ%2BKYzWpWmfy0G7u1bW9%2FDFBnp%2FdGar2GiUYf8RtQVpHd7L9uba70rhd%2Fw3qrcrf1crRWN%2FaPtJu0dKbaW7LWHZWJL8RUfv1%2BH3A0rAysGlHocElm6RypVHMtbqi99pqBzT8sM74O5P4cmMf%2FYZR5UGbC8RyM5LAQBJDAItDnrJamT%2B2hoS1Vt26e51HmOoM%2FjrToGMe2TqKoVNIvLs%2BwtNqGRcAPdN69RSZOswJKk9mJhRnaV1GSVOXCvfv9egNyrveDDgXREmEUrFn6ClZbOhC5ab6et33a0mhjrg%2FB1jrj9ZpE5MhZNsiamPZbdOHJwBN08IWZctTN%2Bsi3Xw4tpvhKakEZ2CgCAfB3d5vBXGAvEUF69i3ZSgBKDsqAouixQnquv6QXYiPynexKavNG0OWC%2FXuGKBm4zzGR4t7yf3H7nbf2yRoSGQznXFU3tqEsHxUPN2%2Bh%2F5ARMLii7eg7SpHeceHEo0Lx9Ys8n1G1MiLNSz58V7JxkpqEe1cM4uHXLl3DJV3W6B5kTTuY572GSMOq3ndMGOqUBzpVRNEb9OBxmVnffw4%2BFjoCmgv2NPfj9NTmsVQALsdRV9xbzLBV7xN1HsOD9P%2B0wE2hRJtXjI%2B4mUgJuHsXc%2FL%2BMy4XWOpMElarFLt4cH1P%2F1VX9%2FIRZD%2F1ebe2zpAE%2FC1%2F4LyHsNEvFxab8ktqT%2F5E7bJ0tB1H6NUWynu%2BC5xaZfa2NEgLcf8z9Urh2xazTsmkOfPqncnphAJTOGTET0SAWgIpU&X-Amz-Signature=f8d5c2018ff593d72e972415de845f838effbaf47c4a23de7811e97bcf55a4d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RCOFMAG%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T142019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFOAqNeQXQ9rYaZjZkvmWwO0Kbc7bfHOIyAeiY13x5uPAiEAtsJetJC5ctr3271iDxdBPoY%2BlqFb0VkXeQ3z0p7Jg6Mq%2FwMIThAAGgw2Mzc0MjMxODM4MDUiDBjXGgCawbm2NujaiircA8cAg57HdI%2Bhe3jnq8HIxGaoqXL2ehahNY8F5eboIC7XkFs7PazBNb9THv4Pk%2Buf6gc5qi50GbCh%2FGTXFLdkT0%2Bjoy9IRXb7JHg9UDkQ%2BKYzWpWmfy0G7u1bW9%2FDFBnp%2FdGar2GiUYf8RtQVpHd7L9uba70rhd%2Fw3qrcrf1crRWN%2FaPtJu0dKbaW7LWHZWJL8RUfv1%2BH3A0rAysGlHocElm6RypVHMtbqi99pqBzT8sM74O5P4cmMf%2FYZR5UGbC8RyM5LAQBJDAItDnrJamT%2B2hoS1Vt26e51HmOoM%2FjrToGMe2TqKoVNIvLs%2BwtNqGRcAPdN69RSZOswJKk9mJhRnaV1GSVOXCvfv9egNyrveDDgXREmEUrFn6ClZbOhC5ab6et33a0mhjrg%2FB1jrj9ZpE5MhZNsiamPZbdOHJwBN08IWZctTN%2Bsi3Xw4tpvhKakEZ2CgCAfB3d5vBXGAvEUF69i3ZSgBKDsqAouixQnquv6QXYiPynexKavNG0OWC%2FXuGKBm4zzGR4t7yf3H7nbf2yRoSGQznXFU3tqEsHxUPN2%2Bh%2F5ARMLii7eg7SpHeceHEo0Lx9Ys8n1G1MiLNSz58V7JxkpqEe1cM4uHXLl3DJV3W6B5kTTuY572GSMOq3ndMGOqUBzpVRNEb9OBxmVnffw4%2BFjoCmgv2NPfj9NTmsVQALsdRV9xbzLBV7xN1HsOD9P%2B0wE2hRJtXjI%2B4mUgJuHsXc%2FL%2BMy4XWOpMElarFLt4cH1P%2F1VX9%2FIRZD%2F1ebe2zpAE%2FC1%2F4LyHsNEvFxab8ktqT%2F5E7bJ0tB1H6NUWynu%2BC5xaZfa2NEgLcf8z9Urh2xazTsmkOfPqncnphAJTOGTET0SAWgIpU&X-Amz-Signature=a2a2542c64715c749b7ee265bc9899111abf97170e2b0fdbf9837e41a66331b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







