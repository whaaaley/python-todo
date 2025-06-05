import { RiCheckboxBlankLine, RiCheckboxLine } from '@remixicon/vue'
import { useMutation, useQuery } from '@tanstack/vue-query'
import { defineComponent, ref } from 'vue'
import client from './client'

type Todo = {
  id: number
  title: string
  completed: boolean
}

const TodoItem = defineComponent({
  name: 'TodoItem',
  props: {
    id: {
      type: Number,
      required: true,
    },
    tile: {
      type: String,
      required: true,
    },
    completed: {
      type: Boolean,
      required: true,
    },
  },
  emits: ['success'],
  setup (props, { emit }) {
    const { mutate } = useMutation({
      mutationFn: async () => {
        const { data } = await client.PUT('/todo/update/{todo_id}', {
          params: {
            path: { todo_id: props.id },
          },
          body: {
            completed: !props.completed,
          },
        })
        return data
      },
      onSuccess: () => {
        emit('success')
      },
    })

    return () => (
      <div class='flex gap-2'>
        <button onClick={() => { mutate() }}>
          {props.completed ? <RiCheckboxBlankLine/> : <RiCheckboxLine/>}
        </button>
        <div>{props.id}</div>
        <div>{props.tile}</div>
      </div>
    )
  },
})

const ListTodos = defineComponent({
  name: 'ListTodos',
  setup (_props, { expose }) {
    const { data: todos, refetch } = useQuery({
      queryKey: ['todos'],
      queryFn: async () => {
        const { data } = await client.GET('/todo/list')
        return data || []
      },
      initialData: [],
    })

    expose({ refetch })

    return () => (
      <div class='grid gap-4'>
        {todos.value.map((todo: Todo) => (
          <TodoItem
            key={todo.id}
            completed={todo.completed}
            id={todo.id}
            tile={todo.title}
            onSuccess={() => { refetch() }}
          />
        ))}
      </div>
    )
  },
})

const CreateTodo = defineComponent({
  name: 'CreateTodo',
  emits: ['success'],
  setup (_props, { emit }) {
    const newTodo = ref('')

    const { mutate: createTodo } = useMutation({
      mutationFn: async () => {
        const { data } = await client.POST('/todo/create', {
          body: {
            title: newTodo.value,
            completed: false,
          },
        })
        return data
      },
      onSuccess: () => {
        emit('success')
      },
    })

    return () => (
      <div class='flex gap-2'>
        <input class='text-black' placeholder='New Todo' type='text' v-model={newTodo.value}/>
        <button onClick={() => { createTodo() }}>Add Todo</button>
      </div>
    )
  },
})

export default defineComponent({
  name: 'HomePage',
  setup () {
    const listTodos = ref()

    const onSuccess = () => {
      if (listTodos.value) {
        listTodos.value.refetch()
      }
    }

    return () => (
      <div>
        Python Typed Typed Todo App
        <CreateTodo onSuccess={onSuccess}/>
        <ListTodos ref={listTodos}/>
      </div>
    )
  },
})
