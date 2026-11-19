



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRYSVDLS%2F20261119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261119T120711Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaCXVzLXdlc3QtMiJGMEQCIH1HP4dEIrX9AqYLIlwh%2BCsxqnlLmJIpR5QgNagzupU6AiAaawumn5os8ISDrXZuvLU6iSDTa8N%2BzmS%2FExO3oBA8Gyr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIM18kjkJDpxqZEGn3YKtwD%2Fh8J0Yy4ktSy9Wt%2Bl67Lf6KxFiRxkdFVK6BqS7YNVQyRjvOchuOKCKYvWc4P3MY83wkooxmmwl55JuxibIk5TFnudQOiZZ4WAsFdltDrbIGKp3OCPQB9CcnHxqah9KhNSjPjArMx1nq3n9XQ4%2B4AmWezP6fIegMfoIkjn0m2R%2BPqt9KbvFot2JcqmcZ8mmINWk9dT42dRzBSM9ySpNSxMDHxGGK9gVtb2PQLf5zAR4A%2BoIKSz%2Bm8CzXU5ykgy6bA0lfc3LmlwRCJ08NwhuE80R6pX8DBoaiT7J%2BB3wuqjy242wfxD8aVdz7yQSWxJx7gE3CdNwvXlu8W1pxddkWzJQgiTS9zGI2BrFLE3a8rAYTOwJ0Pz%2BwGGE3hAx6J0eqSWewu8yaSw7pnw69naRSYO%2FK1jcar5PqKYormJc2phQbN%2Fjt3l5H5J2QJzYXeXktsX0ufnzkiBKsWqLOHRu2ekCIw4Khjrhpno%2Bc%2BwNslfLTLWiR9KknG7OfZ32c3l2pywQ%2FjeoeZqaUIMLv%2BTOsImxiq13sTJA82KBf8k2Zosnb38OXh%2FfP8vb34%2B2XpAXgekUhOBqOU1dQ6QH2Sco6wm5W9pRY%2FUX9mGVlsvVtawUJKQUzVI7mzpgkIclAwqMH71wY6pgEvAkurL297eMkSf8XuP%2Bh96ak2RCkiXB34kwuxX5sygdiNOXQKVzh%2F%2FsMGVyc6GjhFdG0No9%2Bbzfh3eErdPPb7eIhC686YSVlhhMOZVmS9zhpOyztaWUhYoV0Nnj3vPcKR1y%2F%2BbH1PsYy779095LVnPiMlAFE8K5KSUC42%2Fgg2j6lXySHleWN7P5iZoqLgh3KA7bv99OjnsLxAB%2BfdyQBZL2Q%2FngVF&X-Amz-Signature=ad0343c96a8c1bda86f97e75e915f40b51548407dece17ac99b19a2e638e8c62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRYSVDLS%2F20261119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261119T120712Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaCXVzLXdlc3QtMiJGMEQCIH1HP4dEIrX9AqYLIlwh%2BCsxqnlLmJIpR5QgNagzupU6AiAaawumn5os8ISDrXZuvLU6iSDTa8N%2BzmS%2FExO3oBA8Gyr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIM18kjkJDpxqZEGn3YKtwD%2Fh8J0Yy4ktSy9Wt%2Bl67Lf6KxFiRxkdFVK6BqS7YNVQyRjvOchuOKCKYvWc4P3MY83wkooxmmwl55JuxibIk5TFnudQOiZZ4WAsFdltDrbIGKp3OCPQB9CcnHxqah9KhNSjPjArMx1nq3n9XQ4%2B4AmWezP6fIegMfoIkjn0m2R%2BPqt9KbvFot2JcqmcZ8mmINWk9dT42dRzBSM9ySpNSxMDHxGGK9gVtb2PQLf5zAR4A%2BoIKSz%2Bm8CzXU5ykgy6bA0lfc3LmlwRCJ08NwhuE80R6pX8DBoaiT7J%2BB3wuqjy242wfxD8aVdz7yQSWxJx7gE3CdNwvXlu8W1pxddkWzJQgiTS9zGI2BrFLE3a8rAYTOwJ0Pz%2BwGGE3hAx6J0eqSWewu8yaSw7pnw69naRSYO%2FK1jcar5PqKYormJc2phQbN%2Fjt3l5H5J2QJzYXeXktsX0ufnzkiBKsWqLOHRu2ekCIw4Khjrhpno%2Bc%2BwNslfLTLWiR9KknG7OfZ32c3l2pywQ%2FjeoeZqaUIMLv%2BTOsImxiq13sTJA82KBf8k2Zosnb38OXh%2FfP8vb34%2B2XpAXgekUhOBqOU1dQ6QH2Sco6wm5W9pRY%2FUX9mGVlsvVtawUJKQUzVI7mzpgkIclAwqMH71wY6pgEvAkurL297eMkSf8XuP%2Bh96ak2RCkiXB34kwuxX5sygdiNOXQKVzh%2F%2FsMGVyc6GjhFdG0No9%2Bbzfh3eErdPPb7eIhC686YSVlhhMOZVmS9zhpOyztaWUhYoV0Nnj3vPcKR1y%2F%2BbH1PsYy779095LVnPiMlAFE8K5KSUC42%2Fgg2j6lXySHleWN7P5iZoqLgh3KA7bv99OjnsLxAB%2BfdyQBZL2Q%2FngVF&X-Amz-Signature=1d2899857e31e628445987610e65764aca3d1dc941a66247375bc800c873e1f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







