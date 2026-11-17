



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HFS6ZVW%2F20261117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261117T120706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJGMEQCIAPfxWaOnRjzE86eoiBH5p4OBmfebXA0LdEUaTzKHsprAiBdoaifbgEqfsYOhQwaug5T7qi9SEjHp%2Bh4pv5MxozjQSqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrMJqa0kau0h2p%2BhXKtwDfZhbdLyJFsuAKIVBo1yi75%2BhidB0nLM%2BKyodwsMBH4PoVfj2JqROm8JUIridngzRxoSjgCmwHKbUGEOb8crTYeDIR1VL25ZNjrQeE2A%2FWMF3uaK12It5te%2B47tfA3qSsU9AncywbVcIQdAli9HMXo7q4XbQtchyWWvR3MZ1kvM94w0%2BYAxIF3NVFTfyeJTKG3xEDrxuP92NGYjci4sbx0Pp1MEPRTbb7OEdpn%2BPUh4ywCPN7MSWNbdrz%2FTwjyqkm40TnKsJ0079SQUoumSmfXi2rHRRtZ2%2BxOv%2FyrIH%2FmTXugZQ7QMCZZRfzl7Om33AGAKrx525TQpXugFKq6NAgwudNmALFzCSwJhyp1N%2BkShxYRotE2osEEFeQN3jIwKsfyjTaVIvDaByAhlUWJVjRbKu9KsouTkk8HheN1u7oFUYgBYuCd7LaaFG5m2ndQwRqZAQNVaVduWXqeCVMRYDeGupQbNxNNJzEy5yPrV8ousXXIFOfZ4rinjKJ92X8jKArysj0JKWyTFVV%2FzMUkpQ7N6nwRUefiLsPVYTKgiJlBIuf3vH%2BvGZCsrTxXAsN%2F07cqJJocTbUM9SkUNbaQ3kMAdZs7%2F%2BcITLUInL0hlPTLIfTsnghAYXfsPcjPN0wkurw1wY6pgFGaEU%2FncAjY8APq5JOyxBO7gEOX6Hdgl8Nt0iDNP8tNSV2f0SXMGoCxcaGWnUSARFy9fo1mgeu5ZIywAIQm%2FLRI8XKer0sBf9fstmHwBDURFh9Y7ynpZ0yhUkN4bsjuDoSVOBnYAg3PMkOskZplMt28Oq9yVHFSwCmH8Bmgv8bd%2BCSMgwUagUmNobdv9VeQz1OdqFdK8b1sZgG44sbggvF4JTG8a7%2B&X-Amz-Signature=cf9da9e8b682ed3c8ec0b8827f41c7c133d3e01271e744ad0fb680252630f3fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HFS6ZVW%2F20261117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261117T120706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJGMEQCIAPfxWaOnRjzE86eoiBH5p4OBmfebXA0LdEUaTzKHsprAiBdoaifbgEqfsYOhQwaug5T7qi9SEjHp%2Bh4pv5MxozjQSqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrMJqa0kau0h2p%2BhXKtwDfZhbdLyJFsuAKIVBo1yi75%2BhidB0nLM%2BKyodwsMBH4PoVfj2JqROm8JUIridngzRxoSjgCmwHKbUGEOb8crTYeDIR1VL25ZNjrQeE2A%2FWMF3uaK12It5te%2B47tfA3qSsU9AncywbVcIQdAli9HMXo7q4XbQtchyWWvR3MZ1kvM94w0%2BYAxIF3NVFTfyeJTKG3xEDrxuP92NGYjci4sbx0Pp1MEPRTbb7OEdpn%2BPUh4ywCPN7MSWNbdrz%2FTwjyqkm40TnKsJ0079SQUoumSmfXi2rHRRtZ2%2BxOv%2FyrIH%2FmTXugZQ7QMCZZRfzl7Om33AGAKrx525TQpXugFKq6NAgwudNmALFzCSwJhyp1N%2BkShxYRotE2osEEFeQN3jIwKsfyjTaVIvDaByAhlUWJVjRbKu9KsouTkk8HheN1u7oFUYgBYuCd7LaaFG5m2ndQwRqZAQNVaVduWXqeCVMRYDeGupQbNxNNJzEy5yPrV8ousXXIFOfZ4rinjKJ92X8jKArysj0JKWyTFVV%2FzMUkpQ7N6nwRUefiLsPVYTKgiJlBIuf3vH%2BvGZCsrTxXAsN%2F07cqJJocTbUM9SkUNbaQ3kMAdZs7%2F%2BcITLUInL0hlPTLIfTsnghAYXfsPcjPN0wkurw1wY6pgFGaEU%2FncAjY8APq5JOyxBO7gEOX6Hdgl8Nt0iDNP8tNSV2f0SXMGoCxcaGWnUSARFy9fo1mgeu5ZIywAIQm%2FLRI8XKer0sBf9fstmHwBDURFh9Y7ynpZ0yhUkN4bsjuDoSVOBnYAg3PMkOskZplMt28Oq9yVHFSwCmH8Bmgv8bd%2BCSMgwUagUmNobdv9VeQz1OdqFdK8b1sZgG44sbggvF4JTG8a7%2B&X-Amz-Signature=720f5673a6fc4914c8971685652fc64fb7c19a5aae685fe496c3291e2add5f2f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







