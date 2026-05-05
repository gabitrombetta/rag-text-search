def print_results(results: list):
    for query_results in results:
        if not query_results:
            continue
        print(f'Query: {query_results[0]['query']}')

        for i, r in enumerate(query_results, 1):
            print(f'Top {i}')
            print(f"Documento: {r['document']}")
            print(f"Score: {r['score']:.4f}")
            print(f"Texto:\n{r['text']}")