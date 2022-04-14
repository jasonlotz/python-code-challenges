def get_index_different_char(chars):
    alpha_idx, non_alpha_idx = [], []

    for i, char in enumerate(chars):
        char = str(char)

        if char.isalnum():
            alpha_idx.append(i)
        else:
            non_alpha_idx.append(i)

    return alpha_idx[0] if len(alpha_idx) < len(non_alpha_idx) else non_alpha_idx[0]
