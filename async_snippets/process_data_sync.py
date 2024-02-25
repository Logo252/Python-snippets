async def process_data_sync(data_queue):
    process_data = []
    try:
        while True:
            data = await data_queue.get()
            if data is None: # Sentinel value to stop the loop
                break
            process_data.append(process_data(data))
    except Exception as e:
        log_error(e)
    return process_data