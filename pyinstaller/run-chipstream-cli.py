if __name__ == "__main__":
    import multiprocessing as mp

    from chipstream import cli

    mp.freeze_support()

    cli.main()
