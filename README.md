



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP2I6VQZ%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T012510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDfE1cQBa%2BrVCW1X%2FJvArOQnZfNRyXYH32kF7Cxl8oC6AIgIxMu%2FUn7uEOl8n4jdFOsOonAohCDLAuy1h0CtvyB1QEq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDM9bDF%2FHjAamu4WpdircA0KcfyQAe3B8yUlvSe2miu2dL%2B7BoChNtOAWLSKwf5DrNpKnbi%2BdEnmRRvvKYj0%2B6SS8BBy8a9Bo5KCM6vW9e7a6uvWub7i7A0AgsqbP%2Fx%2BuLYoQUAiQNiPFeZSKJoA3iy%2FnofsxQ81F1isP2idKeCWZ68m%2FmwQgIxVRURLiGhjQXs3oMX2%2B%2FofsQIWN02nhy4Ad3%2BvhcTom2%2FH%2BYNW3pmpJNu50RPmGE1F0gBFS8sZf7%2BeNdwFjSgB10K%2FW0a7SR7EZ4De6dPiPeoIMe6JTiUCtvfzttS48KEegwwc7sm3J5sAuhdoTAQoo6w9Mz03hl9AXJLtfK7OX%2BYpWyo92WPvui01RvjUg7UQZTutUaOQ8F9c%2FKoe7clqupqg5mgO5E7tesNwSI8Ubbuq64zu4e06tC1tw%2BPq2zbg5theHKZ%2FpREPP5Mit8Q%2BlK5T0iC%2BRBDXFojFT9PvNdB175H8WWnnO6KFS49XkSVyAt3oDL%2F%2Fw7oMjhh0YKeZjjyk2HbtSs0JQgeUmDGGYFNsw8MdB%2FQF1Lq0AbC99GmJjr0127iu4M%2BuEiv9t8pDzFv7NjZcBolhkN98wekO1n0zVyVslLpCnTNjjeRkidKtL53dEGObqkZ0ltH2ulT0Qii1zMOTuwcoGOqUB%2BrntZYwf4WrwkCsHabNLUyktgu5aV4%2FcNFE8Ia1KBGpuXTpdjULlysjPiTBXiFwnTHieyT0e5HZzxLeO5fLujJAQo57VlBhRqlpe%2FVuOYi0OS75mehKyRXJaaaJZWiPW5L%2ByY40%2FsWvLxQubOo7hF6tgd0hUJxp%2FmbjxQtVKFT2E8e4tWN6bn4fiENBBr9LeOpNgUT8%2Fx6td3AasosM9Vvb1nwZy&X-Amz-Signature=37476582001920948cb0ae09fdf72e98c6befa4548ad715570ae0083b718bef5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP2I6VQZ%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T012510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDfE1cQBa%2BrVCW1X%2FJvArOQnZfNRyXYH32kF7Cxl8oC6AIgIxMu%2FUn7uEOl8n4jdFOsOonAohCDLAuy1h0CtvyB1QEq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDM9bDF%2FHjAamu4WpdircA0KcfyQAe3B8yUlvSe2miu2dL%2B7BoChNtOAWLSKwf5DrNpKnbi%2BdEnmRRvvKYj0%2B6SS8BBy8a9Bo5KCM6vW9e7a6uvWub7i7A0AgsqbP%2Fx%2BuLYoQUAiQNiPFeZSKJoA3iy%2FnofsxQ81F1isP2idKeCWZ68m%2FmwQgIxVRURLiGhjQXs3oMX2%2B%2FofsQIWN02nhy4Ad3%2BvhcTom2%2FH%2BYNW3pmpJNu50RPmGE1F0gBFS8sZf7%2BeNdwFjSgB10K%2FW0a7SR7EZ4De6dPiPeoIMe6JTiUCtvfzttS48KEegwwc7sm3J5sAuhdoTAQoo6w9Mz03hl9AXJLtfK7OX%2BYpWyo92WPvui01RvjUg7UQZTutUaOQ8F9c%2FKoe7clqupqg5mgO5E7tesNwSI8Ubbuq64zu4e06tC1tw%2BPq2zbg5theHKZ%2FpREPP5Mit8Q%2BlK5T0iC%2BRBDXFojFT9PvNdB175H8WWnnO6KFS49XkSVyAt3oDL%2F%2Fw7oMjhh0YKeZjjyk2HbtSs0JQgeUmDGGYFNsw8MdB%2FQF1Lq0AbC99GmJjr0127iu4M%2BuEiv9t8pDzFv7NjZcBolhkN98wekO1n0zVyVslLpCnTNjjeRkidKtL53dEGObqkZ0ltH2ulT0Qii1zMOTuwcoGOqUB%2BrntZYwf4WrwkCsHabNLUyktgu5aV4%2FcNFE8Ia1KBGpuXTpdjULlysjPiTBXiFwnTHieyT0e5HZzxLeO5fLujJAQo57VlBhRqlpe%2FVuOYi0OS75mehKyRXJaaaJZWiPW5L%2ByY40%2FsWvLxQubOo7hF6tgd0hUJxp%2FmbjxQtVKFT2E8e4tWN6bn4fiENBBr9LeOpNgUT8%2Fx6td3AasosM9Vvb1nwZy&X-Amz-Signature=a31f9a465d4b0e137fff3e04de75244767395e29561148d72dc1a1c5fc61f09f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







