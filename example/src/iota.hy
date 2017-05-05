(defn iota [m &optional [n 0] [step 1]]
  (if (>= n m)
    None
    (cons n (iota m (+ n step) step))))

