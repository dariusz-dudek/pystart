def gradient(procent: float) -> str:
    if procent < 0.45:
        return 'niedostateczny'
    if procent < 0.55:
        return 'dopuszczający'
    if procent < 0.8:
        return 'dostateczny'
    if procent < 0.9:
        return 'dobry'
    if procent < 0.95:
        return 'bardzo dobry'
    return 'celujący'

